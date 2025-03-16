import cv2
import numpy as np

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\klon.jpg",0)
row,col = img.shape
#2 boyutta yön değiştirme  # 90 derece ölçek 1
M= cv2.getRotationMatrix2D((col/2,row/2),90,1)

dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()