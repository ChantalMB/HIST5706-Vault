from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="data")
trainer.setTrainConfig(object_names_array=["img"], batch_size=4, num_experiments=100, train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()