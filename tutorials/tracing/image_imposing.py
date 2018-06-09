# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:28:08 2018

@author: arden
"""

import numpy as np
import cv2

#img loading
img1 = cv2.imread('../images/eyes/sample_1.jpg')
img2 = cv2.imread('../images/eyes/sample_2.jpg')

rows, cols, channels = img2.shape

roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#thresholding(img, thresh, transform, style)
#if above 200 convert to 255, else convert black
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, ori, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst 

cv2.imshow('res', img1)


#cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
#image thresholding