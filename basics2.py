# drawing shapes and putting text

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3),
                 dtype='uint8')  # uint8 is for images and (500,500) depicts shape , 3-> no. of color channels
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0, 255, 0  # BGR
cv.imshow('Green', blank)

# 2.Draw a rectangle
cv.rectangle(blank, (50, 50), (250, 400), (0, 255, 0),
             thickness=2)  # if you want to fill the rectangle with color put thickness = -1 or cv.FILLED
cv.imshow('Rectangle', blank)

# 3.Draw a Circle

cv.circle(blank, (200, 200), 50, (255, 0, 0), thickness=-1)
cv.imshow('Circle', blank)

# 4.Draw a line
cv.line(blank, (100, 100), (200, 100), (0, 0, 255), thickness=2)
cv.imshow('Line', blank)

# 5.Write Text
cv.putText(blank, 'Rishi Jain', (50, 50), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0, 255, 255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
