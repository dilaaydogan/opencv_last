# iki görüntüyü işleyerek farklı sonuçlar üretmek

import cv2
import numpy as np

img1 = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\bitwise_1.png")
img2 = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\bitwise_2.png")

bit_and = cv2.bitwise_and(img2,img1) # Sadece her iki görüntüde de beyaz olan alanlar korunur, diğer alanlar siyah olur.
bit_or = cv2.bitwise_or(img2,img1)  # Görüntülerin birleşimi oluşturulur.
bit_xor = cv2.bitwise_xor(img2,img1) # Sadece birinde olup diğerinde olmayan kısımlar korunur.
bit_not = cv2.bitwise_not(img1)   #Görüntünün negatifini oluşturur.
bit_not2 = cv2.bitwise_not(img2)  #Görüntünün negatifini oluşturur.

cv2.imshow("img",img1)
cv2.imshow("bit_not",bit_not2)


cv2.waitKey(0)
cv2.destroyAllWindows