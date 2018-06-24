import numpy as np
import cv2

class Plot :
    def disp(self, List):
        img = np.zeros((512,512,3), np.uint8)
        for i in range(0, len(List)-1):
	   img = cv2.line(img,(List[i][0], List[i][1]), (List[i+1][0], List[i+1][1]), (0,255,0), 5)
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
