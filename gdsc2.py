import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# Draw rectangle on the blank image
cv2.rectangle(blank, (20, 20), (230, 250), (255, 0, 0), thickness=2)

# Draw text on the blank image
cv2.putText(blank, "Rishi", (30, 130), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), thickness=3)

# Display the updated image in a single window
cv2.imshow("Updated Image", blank)

cv2.waitKey(0)
