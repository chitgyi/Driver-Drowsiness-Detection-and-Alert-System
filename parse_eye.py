# import the necessary packages
# re is regular expression package for search strings with 
# regular expression
import re

# integer indexes that belong to the eyes
LANDMARKS = set(list(range(36, 48)))

# to easily parse out the eye locations from the XML file
# utilize regular expressions to determine if there is a 'part'
PART = re.compile("part name='[0-9]+'")

# path of input datasets it have 68 landmarks
# output and input path for training
inputPath4Train =  "datasets/labels_ibug_300W_train.xml"
outputPath4Train = "datasets/labels_ibug_300W_train_eyes.xml"

# output and input path for testing
inputPath4Test =  "datasets/labels_ibug_300W_test.xml"
outputPath4Test = "datasets/labels_ibug_300W_test_eyes.xml"

# load 68 landmarks XML file  and then split into array like line  by line
rows4Train = open(inputPath4Train).read().strip().split("\n")
rows4Test = open(inputPath4Test).read().strip().split("\n")

# create or update data for inserting eye locations into xml file
# outputs of eye landmarks xml for training
output4Train = open(outputPath4Train,"w")

# outputs of eye landmarks xml for testing
output4Test = open(outputPath4Test,"w")

# loop over the rows of the data split file for training
print("[INFO] Parsing eye landmarks from 68 facial landmarks for training")
for row in rows4Train:
    # check to see if the current line has the (x, y)-coordinates for
    # the facial landmarks we are interested in
    parts = re.findall(PART, row)

    # if there is no information related to the (x, y)-coordinates of
    # the facial landmarks, we can write the current line out to disk
    # with no further modifications
    if len(parts) == 0:
        output4Train.write("{}\n".format(row))

    # otherwise, there is annotation information that we must process
    else:
        # parse out the name of the attribute from the row
        attr = "name='"
        i = row.find(attr)
        j = row.find("'", i + len(attr) + 1)
        name = int(row[i + len(attr):j])

        # if the facial landmark name exists within the range of our
        # indexes, write it to our output file
        if name in LANDMARKS:
            output4Train.write("{}\n".format(row))
print("[INFO] Parsed eye landmarks for training")

# close the output file
output4Train.close()


# loop over the rows of the data split file for testing
print("[INFO] Parsing eye landmarks from 68 facial landmarks for testing")
for row in rows4Test:
    # check to see if the current line has the (x, y)-coordinates for
    # the facial landmarks we are interested in
    parts = re.findall(PART, row)

    # if there is no information related to the (x, y)-coordinates of
    # the facial landmarks, we can write the current line out to disk
    # with no further modifications
    if len(parts) == 0:
        output4Test.write("{}\n".format(row))

    # otherwise, there is annotation information that we must process
    else:
        # parse out the name of the attribute from the row
        attr = "name='"
        i = row.find(attr)
        j = row.find("'", i + len(attr) + 1)
        name = int(row[i + len(attr):j])

        # if the facial landmark name exists within the range of our
        # indexes, write it to our output file
        if name in LANDMARKS:
            output4Test.write("{}\n".format(row))
print("[INFO] Parsed eye landmarks for testing")

# close the output file
output4Test.close()
