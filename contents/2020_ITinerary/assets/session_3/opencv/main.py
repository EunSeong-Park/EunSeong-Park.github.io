import cv2

img = cv2.imread("cat-5249724_1280.jpg", cv2.IMREAD_COLOR)
cv2.imwrite("mycutecat.png", img)

