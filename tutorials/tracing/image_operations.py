# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:52:58 2018

@author: arden
"""

import numpy as np
import cv2

img = cv2.imread('../images/eyes/sample_1.jpg', 1)

#referencing specific pixel (gives array of bgr)
px = img[55,55]

#modify pixels
img[55,55] = [255,255,255]
#to check conversion
print(img[55,55])

#region of image
roi = img[100:150, 100:150]

#copy pasting regionregion
img[0:50,0:50] = roi
