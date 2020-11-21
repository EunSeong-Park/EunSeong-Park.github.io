import cv2



def show(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dot(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(None, (x, y), 5, (255, 0, 0), -1)


cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

while cap.isOpened():
    isSuccess, frame = cap.read()
    if isSuccess:
        cv2.imshow('Video', frame)
        key = cv2.waitKey(1000//60)
        if key == 27:
            break
        elif key == 32:
            print("captured")
            cv2.imwrite("capture/temp1.png", cv2.flip(frame, 1))
cap.release()
cv2.destroyAllWindows()
