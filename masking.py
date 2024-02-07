import cv2
import numpy as np

img = cv2.imread('Photos/cats.jpg')
# cv2.imshow("Cats", img)

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow('Video', frame)

    blank = np.zeros(frame.shape[:2], dtype='uint8')
    cv2.imshow("Blank", blank)

    mask = cv2.circle(blank, (frame.shape[1]//2, frame.shape[0]//2), 150, 255, -1)
    cv2.imshow("Mask", mask)

    masked_video = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("MaskedVideo", masked_video)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

# blank = np.zeros(img.shape[:2], dtype='uint8')
# cv2.imshow("Blank", blank)
#
# mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv2.imshow("Mask", mask)
#
# masked = cv2.bitwise_and(img, img, mask=mask)
# cv2.imshow("Masked", masked)

cv2.waitKey(0)
