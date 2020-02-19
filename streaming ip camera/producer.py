from kafka import KafkaProducer
import sys
import time
import cv2
import pickle
import numpy as np

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],api_version=(0,2,0))

# Open file
video = cv2.VideoCapture('rtsp://yourRTSPlink')

while True:
    success, frame = video.read()

    if not success:
        print("bad read!")
        break

    ret, buffer = cv2.imencode('.jpg', frame)
    producer.send('frame', buffer.tobytes())

    print(buffer.tobytes())
    
video.release()
print('publish complete')

