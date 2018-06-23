import numpy as np
import cv2


list = [[110,12], [150, 60], [150, 480],[102,105], [120, 450] , [ 60,310] , [ 120, 50] , [150,80]]

# Create a black image
img = np.zeros((512,512,3), np.uint8)

for i in range(1,7):
	img = cv2.line(img,(list[i][0],list[i][1]),(list[i+1][0],list[i+1][1]),(0,255,0),5)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

   

