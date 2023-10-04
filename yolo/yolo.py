from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
#import cv2

# Load a model
model = YOLO('yoloModels/yolov8x.pt')  # load an official model

# Predict with the model
#results = model.predict(source='parking.jpg', save=True, conf=0.2)  # predict on an image
results = model.predict(source='test/test3.jpg', save=True, conf=0.25)
print(results)
