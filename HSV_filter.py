import sys
import cv2
import numpy as np
import time 

def add_HSV_filter(frame):

    #Blurring the frame
    blur = cv2.GaussianBlur(frame,(5,5),0)

    #Converting RGB to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])    #Lower limit for red colour in HSV
    upper_red = np.array([179, 255, 255])  #Upper limit for red colour in HSV
 
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    #Morphological operations: Erode followed by Dilate to remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    return mask
