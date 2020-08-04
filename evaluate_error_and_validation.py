import argparse
import dlib

print("[INFO] evaluating shape predictor...")
error = dlib.test_shape_predictor("D:\Thesis\Project\datasets\labels_ibug_300W_test_eyes.xml", "D:\Thesis\Project\custom-dlib-shape-predictor\eye_predictor.dat")
print("[INFO] error: {}".format(error))