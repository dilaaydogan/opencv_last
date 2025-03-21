#bir resimde bulunan çokgenleri (poligonları) tespit edip isimlerini ekrana yazdırır.

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
font1= cv2.FONT_HERSHEY_COMPLEX 

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\polygons.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,threshold = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    epsilon = 0.01*cv2.arcLength(cnt,True) #arcLength → Konturun çevresini hesaplar
    approx = cv2.approxPolyDP(cnt,epsilon,True) #approxPolyDP → Konturu daha düzgün hale getirir ve köşe noktalarını belirler.

    cv2.drawContours(img,[approx],0,(0),5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx)==3:  #len(approx), şeklin kaç kenarı olduğunu belirler.
        cv2.putText(img,"Triangle",(x,y),font1,2,(0))
        
    elif len(approx)==4:
        cv2.putText(img,"Rectangle",(x,y),font1,2,(0))
        
    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x,y),font1,2,(0))
        
    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x,y),font1,2,(0))
        
    else:
        cv2.putText(img,"Ellipse",(x,y),font1,2,(0))

cv2.imshow("IMG",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
        


