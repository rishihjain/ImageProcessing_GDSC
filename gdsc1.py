import cv2

img = cv2.imread('Photos/cats.jpg')
cv2.imshow("Cat", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

blur = cv2.GaussianBlur()

# def rescaleFrame(img, scale =0.2):
#     width = int(img.shape[1]*scale)
#     height = int(img.shape[0]*scale)
#     dim = (width, height)
#     return cv2.resize(img, dim)
#
# capture = cv2.VideoCapture('Videos/video.mp4')

# while True:
#     success , frame = capture.read()
#     cv2.imshow("Video", frame)
#     frame_resize = rescaleFrame(frame, scale=0.2)
#     cv2.imshow("Frame_resized", frame_resize)
#
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
#
# capture.release()
# cv2.destroyAllWindows()

cv2.waitKey(0)
