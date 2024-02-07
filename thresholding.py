import cv2

img = cv2.imread('Photos/cats.jpg')
cv2.imshow("Cats", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Simple Thresholding
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Simple Thresholding", thresh)

threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Inv Thresholding", thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 13, 9)
cv2.imshow("Adaptive Thresholding", adaptive_thresh)

cv2.waitKey(0)
