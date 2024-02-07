import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Photos/park.jpg')
cv2.imshow("Park", img)  # displays in BGR format

plt.imshow(img)  # displays RGB image format
plt.show()

# BGR to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", gray)

# BGR to HSV(Hue Saturation Value)
# In traffic sign recognition, converting BGR to HSV can help in isolating the color of the traffic signs. #
# Hue is particularly useful for detecting specific colors, such as red for stop signs. #
# Saturation and Value channels can be employed to fine-tune the color segmentation.
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv)

# BGR to L*a*b (L- lightness , a- Green to Magenta and b- Blue to Yellow)
# In medical image analysis, converting BGR to LAB can be useful for tasks like tissue detection.
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
cv2.imshow("Lab", lab)

cv2.waitKey(0)
