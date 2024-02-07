"""Contours can be explained simply as a curve joining all the continuous points (along the boundary),
having same color or intensity. The contours are a useful tool for shape analysis and object detection
and recognition."""

import cv2
import numpy as np

img = cv2.imread('Photos/hand.jpg')
cv2.imshow("Cats", img)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow("Blank", blank)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImg", gray)

blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow("Blur", blur)

canny = cv2.Canny(img, 125, 175)
cv2.imshow("Canny", canny)

ret, thresh = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholding", thresh)
print(ret)

# adaptive_thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                         cv2.THRESH_BINARY, 13, 9)
# cv2.imshow("Adaptive Thresholding", adaptive_thresh)

contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.imshow("Contours",contours)
print(f'{len(contours)} contours found')
print(hierarchies)

cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
cv2.imshow("Contours Drawn", img)

cv2.waitKey(0)
