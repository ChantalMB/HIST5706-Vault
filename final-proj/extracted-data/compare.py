import os
import shutil

with open('illudet-comp.txt') as f:
    lines = f.read().splitlines()

illu_detections = []
for i in lines:
    img_name = i.split('/')
    illu_detections.append(img_name[2])

my_detections = []
for file in os.listdir('/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original'):
    my_detections.append(file)

comp = []
for i in illu_detections:
    if i not in my_detections:
        comp.append(i)

for j in comp:
    j = '/home/cbrou/Desktop/YODH-project/annotating-training-imgs/images/' + j
    shutil.copy(j, "/home/cbrou/Desktop/missing/")