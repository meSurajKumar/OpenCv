import cv2
## This is for check the camera(web or any external camera.)

frame_width = 640
frame_height = 480
cap =cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)

while True:
    success , img = cap.read()
    cv2.imshow("Video" , img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break