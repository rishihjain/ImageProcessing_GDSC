import cv2

img = cv2.imread('Photos/cats.jpg')
cv2.imshow("Cats", img)

# Average Blur
avg = cv2.blur(img, (7, 7))
cv2.imshow("Avg Blur", avg)

# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow("Gaussian Blur", gaussian)

# Median Blur
median = cv2.medianBlur(img, 7)
cv2.imshow("Median Blur", median)

# Bilateral Blurring  # most effective blurring method .It blurs the image but retains the edges inside the image
bilateral = cv2.bilateralFilter(img, 15, 55, 45)
cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)
