# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 08:29:52 2018

@author: arden
"""

import cv2
import numpy as np

#use GUI for near perfect match detection

img_bgr = cv2.imread('../images/eyes/sample_1.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('../images/eyes/template_1.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res > threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
    
cv2.imshow('detected', img_bgr)
