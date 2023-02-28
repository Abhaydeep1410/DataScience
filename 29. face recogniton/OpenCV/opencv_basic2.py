import cv2

img=cv2.imread('dog.png')

gray=cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('dog title',img)
cv2.imshow('gray dog title',gray)
cv2.waitKey(0) # means wait for infinite time we can add number also 25 means wait for 25 milisecond 
# program will stop when any key is pressed

cv2.destroyAllWindows()