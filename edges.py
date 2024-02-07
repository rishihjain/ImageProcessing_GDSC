import cv2
import numpy as np

img = cv2.imread('Photos/car.jpg')
cv2.imshow("Park", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Laplacian Edge Detection
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

# Sobel
sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

cv2.imshow("SobelX", sobelX)
cv2.imshow("SobelY", sobelY)

Combined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Combined Sobel", Combined)

# Canny
canny = cv2.Canny(gray, 150, 175)
cv2.imshow("Canny", canny)



cv2.waitKey(0)
