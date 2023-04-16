import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import concurrent.futures
import torch
import pandas
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
import time

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

url='http://192.168.137.37/capture?_cb=1681499310297'
im=None
 
def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
 
        cv2.imshow('live transmission',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
        
def run2():
    serialInst = serial.Serial()
    portslist = []

    for onePort in ports:
        portslist.append(str (onePort))
        print (str(onePort))

    val = "5"

    for x in range(0, len(portslist)):
        if portslist[x].startswith("COM" + str(val)):
            portVar = "COM" + str(val)
            print (portVar)


    def sendcmd(cmd):
        time.sleep(2)
        command = cmd
        serialInst.write(command.encode('utf-8'))


    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()

    cv2.namedWindow("YOLO", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        frame = cv2.imdecode(imgnp,-1)
        
        # Make detections 
        results = model(frame)
        car_rows = results.pandas().xyxy[0].loc[results.pandas().xyxy[0]['name'] == 'car']
        
        print("number of cars detected: ",len(car_rows))
        print()
    
        if(len(car_rows) > 4):
            print("green signal issused")
            sendcmd("greenOn")
        else:
            print("stop")
            sendcmd("redOn")

        cv2.imshow('YOLO', np.squeeze(results.render()))
        
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
 
 
 
if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executer:
            f1= executer.submit(run1)
            f2= executer.submit(run2)
