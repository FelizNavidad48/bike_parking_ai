from ultralytics import YOLO
from shee import add_row
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
#import cv2
#Comentaras

# Load a model
model = YOLO('yoloModels/yolov8x.pt')  # load an official model

# Predict with the model
#results = model.predict(source='parking.jpg', save=True, conf=0.2)  # predict on an image
results = model.predict(source='test/test2.jpg', save=True, conf=0.25)
resultBoxes = results[0].boxes.cls

#print(str(resultBoxes).count("1"))
add_row(11, 6,str(resultBoxes).count("1"))



