import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Converting to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur an image - it reduces the noise/level of detail/sharpness of the image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade - identify boundaries within an image where there is a significant change in intensity or color.
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilation and Erosion - Morphological operations

# Erosion:
#
# Purpose: Erosion is a morphological operation that shrinks or erodes the boundaries of foreground (object) regions.
# How it works: It moves a structuring element (a small kernel) over the image, and for each pixel covered by the kernel, if all the pixels are "1" (white), the center pixel is set to "1"; otherwise, it is set to "0" (black).
# Result: Erosion is often used to eliminate small, isolated noise points and to separate objects that are close to each other.
# Dilation:
#
# Purpose: Dilation is a morphological operation that expands or dilates the boundaries of foreground regions.
# How it works: Similar to erosion, it moves a structuring element over the image, and if at least one pixel under the kernel is "1," the center pixel is set to "1"; otherwise, it is set to "0."
# Result: Dilation is useful for closing gaps between edges and connecting broken or disjointed parts of objects in the image.


# Dilation of the image
dilated = cv.dilate(canny, (7, 7), iterations=2)
cv.imshow('Dilated', dilated)

# Erosion of the image
erode = cv.erode(dilated, (7, 7), iterations=2)
cv.imshow('Erosion', erode)

# Resize 
resized = cv.resize(img, (800, 700), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[150:300, 300:600]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
