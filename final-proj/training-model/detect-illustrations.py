import os
import shutil

from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("data/models/detection_model-ex-003--loss-0005.967.h5")
detector.setJsonPath("data/json/detection_config.json")
detector.loadModel()

set_img_dir = os.chdir('/home/cbrou/Desktop/YODH-project/annotating-training-imgs/images/')

for file in os.listdir(set_img_dir):

    annotated_file = "/home/cbrou/Desktop/YODH-project/pgs-with-imgs/annotated/" + os.path.splitext(file)[0] + "-anno.jpg"

    # setting minimum_percentage_probability so low to make sure no ultra faded images are missed, but will filter detections < 10 into their own folder
    detections = detector.detectObjectsFromImage(input_image=file, output_image_path=annotated_file, minimum_percentage_probability=1)

    print("total detections: " + str(len(detections)))
    if len(detections) > 0:
        print("file:" + file)

        og_path = '/home/cbrou/Desktop/YODH-project/annotating-training-imgs/images/' + file

        # check if probability is over 10
        over_10 = False
        for detection in detections:
            if detection["percentage_probability"] >= 10:
                over_10 = True
                break

        if over_10:
            shutil.copy(og_path, "/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original/")
        else:
            shutil.copy(og_path, "/home/cbrou/Desktop/YODH-project/pgs-with-imgs/original/low-probability/")
            shutil.move(annotated_file, "/home/cbrou/Desktop/YODH-project/annotated/low-probability/")
    else:
        os.remove(annotated_file)

    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

    print("-----------")

