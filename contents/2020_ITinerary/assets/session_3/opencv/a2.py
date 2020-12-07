import cv2
import numpy as np
import time
import math


def get_point_on_circle(center, radius, theta):
    return (int(radius * math.cos(theta) + center[0]),
            int(radius * math.sin(theta) + center[1]))



img = np.zeros((600, 600,3), np.uint8)
img[:, :] = [255, 255, 255]

while True:
    tmp_s = (time.time() % 628) * 3
    tmp_m = tmp_s / 60
    tmp_h = tmp_s / 3600

    img = np.zeros((600, 600, 3), np.uint8)
    img[:, :] = [255, 255, 255]

    img = cv2.circle(img, (300, 300), 270, (0, 0, 0), thickness=8)
    img = cv2.circle(img, (300, 300), 5, (0, 0, 0), thickness=-1)
    img_2 = cv2.line(img, (300, 300),
                     get_point_on_circle((300, 300), 250, tmp_s), (0, 0, 255),
                     thickness=2)
    img_2 = cv2.line(img, (300, 300),
                     get_point_on_circle((300, 300), 180, tmp_m), (0, 0, 0),
                     thickness=4)
    img_2 = cv2.line(img, (300, 300),
                     get_point_on_circle((300, 300), 100, tmp_h), (0, 0, 0),
                     thickness=9)

    cv2.imshow("window", img_2)
    if cv2.waitKey(1000 // 30) == 27:
        break

