import os
import numpy as np
import cv2 

#module error coming
image=cv2.imread("121.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("title",image)

#percentage of resizing
scale_percent=50

#taking the height and width of the image to resize
width=int(image.shape[1]*scale_percent/100)
height=int(image.shape[0]*scale_percent/100)

#dsize is the final size of the image
dsize = (width, height)

#resized image
resized_image = cv2.resize(image, dsize)

cv2.waitKey(0)