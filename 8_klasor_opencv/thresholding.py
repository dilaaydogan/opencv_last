#eşikleme

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\klon.jpg",0)

#eğer piksel değeri 127den büyüksen beyaz, küçükse siyah yapılır
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)  #mean olan eşik değeri belirler
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)


cv2.imshow("img", img)
cv2.imshow("img-th1",th1)
cv2.imshow("img-th2",th2)
cv2.imshow("img-th3",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()
