import random
import os

with open('xml_files.txt') as f:
    lines = f.read().splitlines()

# randomly shuffle order of list for ~variety~

random.shuffle(lines)

# create list of data to be moved into "train" folder --> 161 is approx 80% of files
training = []
for i in range(161):
    training.append(lines[0])
    lines.pop(0)


# remaining files in line now what will be put in validation folder
validation = lines

# make iterative txt files for training data
txtfile = open("/home/cbrou/Desktop/YODH-project/data/train/annotations/xml_list.txt", "w")
for file in training:
    txtfile.write(file + "\n")
txtfile.close()

txtfile = open("/home/cbrou/Desktop/YODH-project/data/train/images/img_list.txt", "w")
for file in training:
    new_ext = os.path.splitext(file)[0] + '.jpg'
    txtfile.write(new_ext + "\n")
txtfile.close()

# make iterative txt files for validation data
txtfile = open("/home/cbrou/Desktop/YODH-project/data/validation/annotations/xml_list.txt", "w")
for file in validation:
    txtfile.write(file + "\n")
txtfile.close()

txtfile = open("/home/cbrou/Desktop/YODH-project/data/validation/images/img_list.txt", "w")
for file in validation:
    new_ext = os.path.splitext(file)[0] + '.jpg'
    txtfile.write(new_ext + "\n")
txtfile.close()
