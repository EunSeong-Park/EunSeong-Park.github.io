import cv2

img = cv2.imread('empty.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow("w", img)
cv2.waitKey(0)
