import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

codec = cv2.VideoWriter_fourcc(*"DIVX")
output = cv2.VideoWriter('MyRecording.avi', codec, 30, (640, 480))
recording = False

while cap.isOpened():
    isSuccess, frame = cap.read()
    if isSuccess:

        cv2.imshow('Video', frame)

        key = cv2.waitKey(1000 // 30)
        if recording:
            output.write(frame)

        if key == 27:  # ESC
            output.release()
            break
        if key == 32:  # SpaceBar
            if not recording:
                recording = True
                print("Start recording")
            else:
                recording = False
                print("Pause!")

cap.release()
cv2.destroyAllWindows()

