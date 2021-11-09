import cv2
import numpy as np

## For creating the image

## img = np.zeros((512,512)) ## Explained Below>>>> Why we don't use this.


'''
img = np.zeros((512,512)) ::- This will create a Blank - Black image
But it can only store the white and black color or some intensity of the grayscale because it has only 1 channel.
But we want to draw the color image which has 3 channels
so we use img = np.zeros((512,512,3)) and it has 3 channels and it can store the all colors.

'''

img = np.zeros((512,512,3)) ## Having 3 channels
print(img.shape)

# LINE :-
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)

'''
LINE:- cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)

-: For line we use the cv2.line method to draw the line .

-: (img,(0,0),(img.shape[1],img.shape[0]) == Here (img) is the img onwhic we are drawing the shapes ...
   (img,(0,0) :- is the staring position and the (img.shape[1],img.shape[0]) is the ending position-
      "you can also use your custom position for taht you hvae to strting and the ending position like this-
       (img,(0,0),(45,60)" this is the x,y position of the point on our blank image.The position of x,y points-
       can be changed to get the desire postion.

-: (0,255,0),2) :::- Here (0,255,0) are the colors and '2' is the intensity (thickness) of the line you can change-
                     them according to your needs.
'''

# Rectangle ::-

# cv2.rectangle(img,(75,45),(95,60),(0,0,255),2)
cv2.rectangle(img,(350,100),(450,200),(0,255,0),cv2.FILLED)

'''
cv2.rectangle(img,(75,45),(95,60),(0,0,255),2) ::- cv2.rectangle method is used.

::- (75,45),(95,60) are the starting and the ending postions, 2 is the thickness,
::- cv2.FILLED IT will fill your image - shapes with color. 
'''

# Circle ::-
cv2.circle(img,(150,400),50,(255,0,0),10)

'''
::- cv2.circle method is used.

::- (150,400) is the center position. 

::- 50 is the radious. and 10 is the thickness od the line. 
'''

# Text ::-
cv2.putText(img,"Prof.ParadoX",(75,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,150,0),1)

'''
::- cv2.putText methos is used.
::- "Prof.ParadoX" is the text.
::- (75,50) is the starting position of the text
::- cv2.FONT_HERSHEY_DUPLEX,1 ::- here cv2.FONT_HERSHEY_DUPLEX is font i used and "1" is the scale of the font
::- (0,150,0) is color
::- 1 is the thickness.

'''

cv2.imshow("blank",img)
cv2.waitKey(0)