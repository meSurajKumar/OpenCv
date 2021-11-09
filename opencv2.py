import cv2

img =  cv2.imread("OpenCV/Penguins.jpg")

'''
imread = for reading the image and video
imshow = for showing the image
waitkey = is to hold the screen , 0 is for infinity time
cv2.imshow('pen',img) : here "pen" is the window and (img is what we want to show)
'''

cv2.imshow("pen",img)
cv2.waitKey(0)