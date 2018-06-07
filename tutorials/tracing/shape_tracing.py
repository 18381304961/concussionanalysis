# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:29:18 2018

@author: arden
"""

import numpy as np
import cv2

img = cv2.imread('../images/eyes/sample_1.jpg', cv2.IMREAD_COLOR)

#paramaters (imread file, start, end, color, line width)
cv2.line(img, (0,0),  (150,150), (255,255,255), 15)
#cv2.rectangle(#same)

#polygon tracing
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
