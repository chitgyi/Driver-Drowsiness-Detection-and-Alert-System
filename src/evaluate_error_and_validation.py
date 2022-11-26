import argparse
import dlib

EYES_TRAIN_DATA_PATH = "./../datasets/labels_ibug_300W_test_eyes.xml"
OUTPUT_MODEL_PATH = "./../assets/eye_predictor.dat"

print("[INFO] evaluating shape predictor...")
error = dlib.test_shape_predictor(EYES_TRAIN_DATA_PATH, OUTPUT_MODEL_PATH)
print("[INFO] error: {}".format(error))