# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:55:51 2018

@author: arden
"""

import cv2
import numpy as np
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0) #0 is first webcam in system

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    
    cv2.imshow('frame',frame) #good to keep original and modify other
    cv2.imshow('gray',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#close camera
cap.release()
out.release()
cv2.destroyAllWindows()
    
