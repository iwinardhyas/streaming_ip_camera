from kafka import KafkaConsumer
import json
import numpy as np
import cv2
import pickle


consumer = KafkaConsumer('frame',
    bootstrap_servers='localhost:9092',
    api_version=(0,2,0))

for msg in consumer:
    # print(msg.value)
    nparr = np.fromstring(msg.value, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    cv2.imshow("tes",img_np)
    cv2.waitKey(1)
