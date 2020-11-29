import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height

codec = cv2.VideoWriter_fourcc(*"DIVX")

out = cv2.VideoWriter("record.avi", codec, 30, (640, 480))
recording = False

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("MY VIDEO RECORDER", frame)

        key = cv2.waitKey(1000 // 30)
        if recording:
            out.write(frame)

        if key == 27: # ESC
            out.release()
            break
        if key == 32: # spacebar
            if not recording:
                recording = True
                print("start recording")
            else:
                recording = False
                print("pause!")

cap.release()
cv2.destroyAllWindows()

