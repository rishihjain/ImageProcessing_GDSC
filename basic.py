import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)


def rescaleFrame(img, scale=0.5):
    # will work for images,videos and live videos
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions)  # we can add 3rd parameter as interpolation = INTER_AREA/INTER_CUBIC


resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

cv.waitKey(0)

# Reading Videos

capture = cv.VideoCapture('Videos/dog.mp4')


def changeRes(widht, height):
    # only works for live videos
    capture.set(3, widht)
    capture.set(4, height)


while True:
    ret, frame = capture.read()
    if not ret:
        print("End of video")
        break

    frame_resized = rescaleFrame(frame, scale=0.5)



    cv.imshow('Video', frame)
    cv.imshow('Video_Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
