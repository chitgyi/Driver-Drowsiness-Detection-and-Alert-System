# Driver-Drowsiness-Detection-and-Alert-System

## Clone Repository

- `git clone https://github.com/chitgyi/Driver-Drowsiness-Detection-and-Alert-System.git`
- `cd Driver-Drowsiness-Detection-and-Alert-System`

## Downloading Datasets

Download [iBUG](http://dlib.net/files/data/ibug_300W_large_face_landmark_dataset.tar.gz) Datasets and extract it and then rename the extracted folder as datasets

## File Structure

- Driver-Drowsiness-Detection-and-Alert-System
  - alarm.mp3
  - detect_drowsiness.py
  - evaluate_error_and_validation.py
  - eye_predictor.dat
  - parse_eye.py
  - train_eye.py
- datasets
  - afw
  - helen
  - ibug
  - ifpw
  - *.xml
  
## Build & Run
  
### For Training Datasets

- `python parse_eye.py`
- `python train_eye.py`
  
### For Detection
- `python detect_drowsiness.py`
  
