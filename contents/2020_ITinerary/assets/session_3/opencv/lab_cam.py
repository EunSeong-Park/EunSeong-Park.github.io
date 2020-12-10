import cv2
import numpy as np

haar_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def list_compare(a, b):
    if len(a) != len(b): return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def get_face_rect(img):
    f = haar_face.detectMultiScale(img,
                                   scaleFactor=1.05,
                                   minNeighbors=5,
                                   minSize=(100, 100),
                                   flags=cv2.CASCADE_SCALE_IMAGE)
    max_wh = 0
    max_wh_rect = (0,0,0,0)
    for t in f:
        if t[2] + t[3] > max_wh:
            max_wh = t[2] + t[3]
            max_wh_rect = t
    if max_wh == 0:
        return (0,0,0,0)
    else:
        return max_wh_rect

def pixelate(img, area):
    x,y,w,h = area
    a = img[y:y+h, x:x+w]
    a = cv2.resize(a, (10, 10))
    a = cv2.resize(a, (w, h), cv2.INTER_AREA)
    img[y:y+h, x:x+w] = a
    # return img

cap = cv2.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        area = get_face_rect(frame)
        if not list_compare(area, (0,0,0,0)):
            pixelate(frame, area)
        cv2.imshow("Window", frame)

        key = cv2.waitKey(1000 // 30)
        if key == 27: # ESC
            break
        if key == 32: # spacebar
            cv2.imwrite("Captured.png", frame)

cap.release()
cv2.destroyAllWindows()

