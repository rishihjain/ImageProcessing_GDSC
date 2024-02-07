import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('Photos/cats.jpg')
cv2.imshow("Cats", img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("GrayScale", gray)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask", masked)

# GrayScale Histogram
# gray_hist = cv2.calcHist([gray], [0], mask, [256], [0, 256])
# plt.figure()
# plt.title('GrayScale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Color Histogram
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv2.waitKey(0)

