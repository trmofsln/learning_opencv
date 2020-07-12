import cv2
'''img=cv2.imread('img_library/mr.modi.jpg',1)
img[300:800,400:900]=(0,255,255)
cv2.imshow('image', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
part=img[100:400,200:500]
cv2.imshow('image',part)
cv2.waitKey(1000)
cv2.destroyAllWindows()'''
#colouring part of image with pixel presesnt at centre of image and convert all others parts to gray
img2=cv2.imread('img_library/mr.modi.jpg',1)
height = img2.shape[0]
width= img2.shape[1]
(b,g,r)=img2[int(width/2),int(height/2)]
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
img2[200:600,300:700]=(b,g,r)
cv2.imshow('photo',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()