import cv2
#print(cv2.__version__)

#read image
#second arg is a flag that describes how images should be read. 1) color, 0) grayscale, -1) alpha channel, loads image as is
img= cv2.imread('lena.jpg', 0)
#prints matrix
print(img)

#print image
#first arg is name of window, second is our image variable
cv2.imshow('image',img)
#number of milliseconds we want to show the image, or 0 to have it wait until closing
cv2.waitKey(0)
cv2.destroyAllWindows()

#write image to a file
#first arg is name of new image, second is our image variable
#cv2.imwrite('lena_copy.png',img)