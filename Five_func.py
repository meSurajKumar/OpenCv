#### The Five Function OF OPENCV2 ::: EVERY OPENCV USER MUST KNOW ####

import cv2
import numpy as np

kernal = np.ones((5,5))

'''
keranal explanation == keranl is basically a matrix by which we can itrate through the image itself to perform
the function.
'''

'''
The important five function of opencv...
'''
framewidth = 640
frameheight = 360

img = cv2.imread("OpenCV/1face.jpg")
# resizeimg = cv2.resize(img,(framewidth,frameheight),0) ## only for example Explained in gray image conversion below.
resizeimg = cv2.resize(img,(framewidth,frameheight))
cv2.imshow("image",resizeimg)

'''
Function 1::::-BGR2GRAY :::-

Gray-image coversion:-

This is for converting the bgr(rgb) image to gray image

For convert your image to grayscale you can directly do this :- 
{img = cv2.imread("OpenCV/Penguins.jpg",0)} 
By addign the zero in the end when we are importing the image.

But if we are using the webcam the we can use the cv2.cvtColor method
'''
imggray = cv2.cvtColor(resizeimg,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",imggray)


'''
Function 2::::-BLUR IMAGE :::-

This is for to Blur the image ::-
imgblur = cv2.GaussianBlur(resizeimg,(5,5),0)

Here (5,5) is the kernal dimension value and the '0' is the sigma value.

'''
imgblur = cv2.GaussianBlur(resizeimg,(5,5),0)
cv2.imshow("blurimg",imgblur)


'''
Function 3::::- EDGE DETECTOR :::-

In most of the opencv projects the edge dection is used.

in the edge detector :- we have the thresh hold parameters by which we can increase the intensity of the line 
( i.e  the thickness of the lines)

'''
imgcanny = cv2.Canny(resizeimg,150,150)


imgcanny2 = cv2.Canny(imggray,150,150)

cv2.imshow("color",imgcanny)
cv2.imshow("Gray",imgcanny2)

'''
Function 4:::- Image dilation :::- 
Is to increae the thickness of the line 
so that we can easily identify the images.
'''
imgDilation = cv2.dilate(imgcanny,kernal,iterations = 1) ## kernal is alreay explained above.

"""
Note:- more itaration will increase the thickness of the line 
"""

cv2.imshow("dilation image " , imgDilation)


'''
Function 5:::- Image Erode :::- 
Is to decrease the thickness of the lines
so that we can easilt identify the images.

'''

imgerode = cv2.erode(imgDilation,kernal,iterations = 2)

"""
Note:- more itaration will decrease the thickness of the line 
"""
cv2.imshow("erodeimage " , imgerode)

cv2.waitKey(0)