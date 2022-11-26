# Driver-Drowsiness-Detection-and-Alert-System

## Clone Repository

- `git clone https://github.com/chitgyi/Driver-Drowsiness-Detection-and-Alert-System.git`
- `cd Driver-Drowsiness-Detection-and-Alert-System`

## Downloading Datasets

Download [iBUG](http://dlib.net/files/data/ibug_300W_large_face_landmark_dataset.tar.gz) Datasets and extract it and then rename the extracted folder as datasets

## File Structure

```
Project
│
└───docs/
|
└───datasets/
│   │   afw/
|   |   helen/
|   |   ibug/
|   |   lfpw/
│   │   *.xml
|   |
└───src/
|   │   alarm.mp3
|   |   detect_drowsiness.py
|   |   evaluate_error_and_validation.py
|   |   parse_eye.py
|   |   train_eye.py
|
└───README.md  
```
  
## Parsing Eyes Features and Train these Eyes Features

```bash
$ ./scripts.sh
```

## Only for drowsiness detection

```bash
cd src
python3 detect_drowsiness.py
```