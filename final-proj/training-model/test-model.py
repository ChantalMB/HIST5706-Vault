from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("data/models/detection_model-ex-031--loss-0001.800.h5")
detector.setJsonPath("data/json/detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="t1.jpg", output_image_path="detected.jpg", minimum_percentage_probability=5)

print(len(detections))
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])