# bash shell

# install dependencies
pip3 install -r requirements.txt

# go to src directory
cd src

# parse eyes landmarks
python3 parse_eyes.py

# train eyes landmarks
python3 train_eyes.py

# evaluate eyes landmarks
python3 evaluate_eyes.py

# detect drowsiness
python3 detect_drowsiness.py
