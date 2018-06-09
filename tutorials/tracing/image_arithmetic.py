# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:16:23 2018

@author: arden
"""

import numpy as np
import cv2

#img loading
img_1 = cv2.imread('../images/eyes/sample_1.jpg')
img_2 = cv2.imread('../images/eyes/sample_2.jpg')

#pure addition of pixels
add = cv2.add(img_1,img_2)

#weighted addition (images and weights, gamma)
weighted = cv2.addWeighted(img_1, 0.6, img_2, 0.4, 0)

cv2.imshow(add)
cv2.waitKey(0)
cv2.destroyAllWindows()
