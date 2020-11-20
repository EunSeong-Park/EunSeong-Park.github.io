import cv2

img = cv2.imread("cat-5249724_1280.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("My cute cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

