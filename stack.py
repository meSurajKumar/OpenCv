import cv2
import numpy as np

image = cv2.imread('OpenCV/Penguins.jpg')

resize = cv2.resize(image,(400,400))
resize1 = cv2.resize(image,(400,400))

stack = np.hstack((resize,resize1))


cv2.imshow('stack', stack)
cv2.waitKey(0)