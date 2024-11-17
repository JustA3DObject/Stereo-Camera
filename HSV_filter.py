import sys
import cv2
import numpy as np
import time 

def add_HSV_filter(frame):

    blur = cv2.GaussianBlur(frame,(5,5),0)

    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([60, 35, 140]) 
    upper_blue = np.array([180, 255, 255])
 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    return mask
