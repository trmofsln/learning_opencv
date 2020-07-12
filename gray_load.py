import cv2
img=cv2.imread('img_library/Modi-Netaji.jpg', 0)
cv2.imwrite('img_created/Modi with Netaji statue.png', img)
img2=cv2.imread('img_created/Modi with Netaji statue.png', 1)
cv2.imshow('netaji-statue',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()