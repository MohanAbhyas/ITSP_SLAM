import numpy as np
import cv2


lis = [[110,12], [150, 60], [150, 480],[102,105], [120, 450] , [ 60,310] , [ 120, 50] , [150,80]]

class Plot :
    def __init__(self,list_):
        self.img = np.zeros((512,512,3), np.uint8)
        # Create a black image
        self.List = list_
        self.length = len(list_)

    def disp(self):
        for i in range(0,self.length-1):
	   self.img = cv2.line(self.img,(self.List[i][0],self.List[i][1]),(self.List[i+1][0],self.List[i+1][1]),(0,255,0),5)
        cv2.imshow('image',u.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

u=Plot(lis) 
u.disp()


