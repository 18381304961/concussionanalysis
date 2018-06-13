# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 08:20:39 2018

@author: arden
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelxx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobelxy = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 80, 80)
    
    cv2.imshow('frame', frame)
#    cv2.imshow('laplacian', laplacian)
#    cv2.imshow('sobelxx', sobelxx)
#    cv2.imshow('sobelxy', sobelxy)
    cv2.imshow('edges', edges)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()