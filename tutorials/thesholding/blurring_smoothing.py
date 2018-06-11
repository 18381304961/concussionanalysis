# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 07:49:20 2018

@author: arden
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    #kernel based smoothing
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(frame, -1, kernel)
    
    #gaussian based blurring
    gaus = cv2.GaussianBlur(frame, (15,15), 0)
    
    #median based blurring (least noisy usually)
    median = cv2.medianBlur(frame, 15)
    
    cv2.imshow('frame', frame)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('gaus', gaus)
    cv2.imshow('median', median)
       
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()