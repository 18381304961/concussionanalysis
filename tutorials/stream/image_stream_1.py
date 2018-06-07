# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:23:39 2018

@author: arden
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#defining an image
#if you don't specify second paramater it will have alpha channel
#grayscale eliminates bgra channels, generally used for image processing
img = cv2.imread('../images/eyes/sample_1.jpg', cv2.IMREAD_GRAYSCALE)

#other option for reading paramaters
    #IMREAD_COLOR = 1,2,3,4...ETC
    #IMREAD_UNCHANGED = -1
    #IMREAD_GRAYSCALE = 0

#using cv to display
cv2.imshow('Title', img)
cv2.waitKey(0) #waits for any key to be pressed
cv2.destroyAllWindows()

#note that matplotlib is rgb, cv2 is bgr
#using matplotlib to display
plt.imshow(img, cmap='gray', interpolation='bicubic')
#can plot directly onto image here
plt.show()

#can save an image using
cv2.imwrite('saved.png', img)