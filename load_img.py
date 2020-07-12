import cv2
img=cv2.imread('img_library/salute_modi.jpg',1)
#reading all pixels of image
#now printing all pixels of image
print("All pixels of given image in matrix form are as follows:\n", img)
#printing dimensions,width,height,channels using img.shape
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
print("width of the image in pixels is: ", width)
print("height of the image in pixels is: ", height)
print("channels present the image is: ", channels)
print("dimensions of the image in pixels is: ", dimensions)
cv2.imshow('modi-image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('img_created/salute_mymodi.png', img)