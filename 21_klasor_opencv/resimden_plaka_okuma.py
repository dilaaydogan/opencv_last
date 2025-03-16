import cv2 
import numpy as np
import pytesseract
import imutils

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\licence_plate.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#gray , çap , sigma color , sigma space
filtered = cv2.bilateralFilter(gray,6,250,250)
edged = cv2.Canny(filtered,30,200)   #min max
#tree mod değeri , chain metod değeri gereksiz yerleri yok eder
contours = cv2.findContours(edged , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
#uygun contur değerleri yakala 
cnts = imutils.grab_contours(contours)
#sorted=sırala , alana göre sırala , tersten sırala , 0dan 10a kadar için
cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:10]
screen = None

for c in cnts:
    #epsilon = doğruluk katsayısı , arclenght konturların yay uzunluğunu bulmak
    epsilon = 0.018*cv2.arcLength(c,True)
    #yaklaşım 
    approx =  cv2.approxPolyDP(c,epsilon,True)
    if len(approx)==4:   #4 köşe varsa dikdörtgendir
        screen = approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask,[screen], 0 , (255,255,255), -1)
new_img = cv2.bitwise_and(img,img,mask = mask)

#beyaz bölgeyi tut 
(x,y) = np.where(mask == 255)
(topx , topy) = (np.min(x), np.min(y))
(bottomx , bottomy) = (np.max(x), np.max(y))
#resmi kırpmak
cropped = gray[topx:bottomx + 1 , topy:bottomy + 1]

text = pytesseract.image_to_string(cropped,lang="eng")
print("detected text:", text)
 


cv2.imshow("gray", gray)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

