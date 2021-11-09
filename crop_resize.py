import cv2

img = cv2.imread("OpenCV/humanface.jpg")

print(img.shape) ## Explained below

cv2.imshow("img",img)

## RESIZE:-

'''
To resize our image fist have to know to current dimension (height , width) of our image.
so for that we use the img.shape method.. To get the current dimension of our image.

dimensions :-(768, 1024, 3)  ::: 768 is our height , 1024 is width and the 3 means it has three channels BGR (Blue , Green , Red) 

'''

width ,  height = 500 , 500 ## This is for the resizing the image

'''
For resizing we need the source image and the height and the width.
'''
imgresize = cv2.resize(img, (width , height))
# cv2.imshow("resizeimg",imgresize)


## Croping ::- 

'''
::- For croping we actually don't need any function because the image itself is matrix and for croping we can define the stating value of x we need and the ending value
    and same for the y. and in that way we can crop our image.

'''
#####################################################

'''
For example we are croping the eyes of the human face.
'''

imgcrop = img[350:450,330:700]
print(imgcrop.shape)
'''
[350:450,330:700] :- here [350:450] is for the height (350) is starting value and the 450 is the ending value

and for width we have [330:700] same here (330) is the starting value and (700) is ending value
you can edit the values according to your needs.

'''

cv2.imshow("croped",imgcrop)



cv2.waitKey(0)