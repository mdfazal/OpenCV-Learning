import cv2 as cv

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xff==('d'):
        break

capture.realease()
cv.destroyAllWindows()
