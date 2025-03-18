import cv2
import numpy as np

path1 = ("C:\\Users\\dila\\Desktop\\opencv.project\\input\\aircraft.jpg")
path2 = ("C:\\Users\\dila\\Desktop\\opencv.project\\input\\aircraft1.jpg")

img1 = cv2.imread(path1)
img1 = cv2.resize(img1,(640,550)) #→ Görsellerin boyutunu 640x550 piksele getirir.

img2 = cv2.imread(path2)
img2 = cv2.resize(img2,(640,550))

img3 = cv2.medianBlur(img1,7) #img1 üzerinde 7x7 piksel boyutunda bir medyan bulanıklık filtresi uygular.


if img1.shape == img2.shape:
    print("same size")
else:
    print("not same")



diff = cv2.subtract(img1,img3) #img1 ve img3 (bulanık versiyon) arasındaki farkı piksel bazında çıkarır.
b,g,r = cv2.split(diff) #cv2.split(diff) → Resmi mavi (B), yeşil (G) ve kırmızı (R) kanallarına ayırır.

#0 olmayan yerleri sayar
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 :
    print("completely equal")  #ğer tüm kanalların 0 olmayan piksel sayısı sıfırsa, resimler tamamen aynıdır 
else:
    print("NOT completely equal")


cv2.imshow("Difference",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()