import cv2

img = cv2.imread('mycutecat.png', cv2.IMREAD_GRAYSCALE)
print(img.shape)
cv2.imshow("w", img)
