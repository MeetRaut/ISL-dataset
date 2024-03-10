import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

cap = cv2.VideoCapture(1) 
detector = HandDetector(maxHands=1)
offset=20  # To draw the pink box a little outside rather than touching te fingers
imgSize=300  #Initially setting it to 300

while True:
    success,img = cap.read()  #Read from capture device and store it in img
    hands,img = detector.findHands(img)
    if hands:
        hand=hands[0]  #Pick first hand if 2 hands are found
        x,y,w,h=hand['bbox']
        
        imgWhite=np.ones((imgSize,imgSize, 3),np.uint8)*255   
        imgCrop= img[y-offset:y+h+offset,x-offset:x+w+offset]
        
        imgCropShape = imgCrop.shape #Matrix of 3 values [height, width, chanel]
        
        aspecRatio= h/w
        
        if aspecRatio>1:
            k = imgSize/h
            wCalc= math.ceil((k*w))
            imgResize=cv2.resize(imgCrop, (wCalc, imgSize)) 
            imgResizeShape = imgResize.shape
            wGap=math.ceil((imgSize-wCalc)/2)
            imgWhite[:, wGap:wCalc+wGap]=imgResize
            
        else:
            k = imgSize/w
            hCalc= math.ceil((k*h))
            imgResize=cv2.resize(imgCrop, (imgSize, hCalc)) 
            imgResizeShape = imgResize.shape
            hGap=math.ceil((imgSize-hCalc)/2)
            imgWhite[hGap+hCalc+hGap,:]=imgResize
            
        
        cv2.imshow("ImageCropped", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
