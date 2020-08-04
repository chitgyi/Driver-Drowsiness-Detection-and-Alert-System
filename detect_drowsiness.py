import imutils
# for reading video source from camera
from imutils.video import VideoStream

# for finding face
from imutils import face_utils

# for define any changes
import imutils

# for define during eye blink
import time

# for ERT algorithm
import dlib

# for display and convert into numpy array
import cv2

# for convert image into numpy array
import numpy as np

# for play emegency sound
import playsound

# initialize dlib's face detector (HOG-based) and then load our
# trained shape predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("eye_predictor.dat")

# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] camera sensor warming up...")
vs = VideoStream(src=0).start()
time.sleep(2.0)


def euclidean_dist(ptA, ptB):
    # compute and return the euclidean distance between the two points
    return np.linalg.norm(ptA - ptB)


def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = euclidean_dist(eye[1], eye[5])
    B = euclidean_dist(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = euclidean_dist(eye[0], eye[3])
    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    # return the eye aspect ratio
    return ear


# loop over the frames from the video stream
EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_FRAMES = 16
# initialize the frame counter as well as a boolean used to
# indicate if the alarm is going off
COUNTER = 0
ALARM_ON = False

while True:
    # grab the frame from the video stream, resize it to have a
    # maximum width of 400 pixels, and convert it to grayscale
    frame = vs.read()
    frame = imutils.resize(frame, width=800)
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    if(len(rects) < 1):
        cv2.putText(frame, "No Face Found", (300, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2,)

    # loop over the face detections
    for rect in rects:
        # convert the dlib rectangle into an OpenCV bounding box and
        # draw a bounding box surrounding the face
        # (x, y, w, h) = face_utils.rect_to_bb(rect)
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # use our custom dlib shape predictor to predict the location
        # of our landmark coordinates, then convert the prediction to
        # an easily parsable NumPy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        rightEye = shape[0:6]
        leftEye = shape[6:]

        rightEAR = eye_aspect_ratio(rightEye)
        leftEAR = eye_aspect_ratio(leftEye)

        ear = (leftEAR + rightEAR) / 2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)

        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if ear < EYE_AR_THRESH:
            COUNTER += 1

            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                if not ALARM_ON:
                    ALARM_ON = True
                # cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                playsound.playsound('alarm.mp3', True)
        else:
            COUNTER = 0
            ALARM_ON = False
        # loop over the (x, y)-coordinates from our dlib shape
        # predictor model draw them on the image
        # for (sX, sY) in shape[6:11]:
        # 	cv2.circle(frame, (sX, sY), 1, (0, 0, 255), -1)
        cv2.putText(frame, "EAR: {:.3f}".format(
            ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2,)

    # show the frame
    cv2.imshow("Drowsiness Detection And Alert System by CYA", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
