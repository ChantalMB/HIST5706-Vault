import os
import shutil

# validated = []
# for file in os.listdir('/home/cbrou/Desktop/YODH-project/pgs-with-imgs/annotated'):
#     img_name = file.split("-")
#     validated.append(img_name[0])
#
# sort_clean_imgs = []
#
#
# for file in os.listdir('/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original/low-probability'):
#     if os.path.splitext(file)[0] not in validated:
#         fp = '/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original/low-probability/' + file
#         shutil.move(fp, "/home/cbrou/Desktop/removed_from_original")
#
#
# for file in os.listdir('/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original'):
#     if os.path.splitext(file)[0] not in validated:
#         fp = '/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original/' + file
#         shutil.move(fp, "/home/cbrou/Desktop/removed_from_original")

original = []
annotated = []

for file in os.listdir('/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original'):
    img_name = os.path.splitext(file)[0]
    original.append(img_name)

for file in os.listdir('/home/cbrou/Desktop/YODH-project/pgs-with-imgs/annotated'):
    img_name = file.split("-")
    img_name = img_name[0]
    annotated.append(img_name)

count = 0
for i in annotated:
    if i not in original:
        i = '/home/cbrou/Desktop/YODH-project/annotating-training-imgs/images/' + i + '.jpg'
        shutil.copy(i, "/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original/")