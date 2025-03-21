import cv2
import numpy as np
import os

img1=cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\coins.jpg")
img2=cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\balls.jpg")

gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#karıncalanmayı önlüyo
img1_blur = cv2.medianBlur(gray1,5)
img2_blur = cv2.medianBlur(gray2,5)

#çözünürlük,daireler arasındaki min mesafe,kenar algılama üst eşiği, daireler arası min mesafe,min max daire yarıçapı
circles = cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1=200,param2=10,minRadius=15,maxRadius=90)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        #i[0],i[1] = daire merkezi , i[2]= yarıçap , renk , kalınlık
        cv2.circle(img1, (i[0],i[1]), i[2], (0,255,0),2)

cv2.imshow("img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()