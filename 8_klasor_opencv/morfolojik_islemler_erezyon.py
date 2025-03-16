import cv2
import numpy as np

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\klon.jpg",0)

#matrisler
kernel = np.ones((5,5),np.uint8)
#isim , dize , 1 kere tekrarlama
erosion = cv2.erode(img,kernel,iterations = 1)
#kalınlaştırma
dilation = cv2.dilate(img,kernel)
#openingde morphologyEx resmin üzerindeki bozulmayı (noktaları) götürüyo
#closeda da ana beyaz resmin içindeki noktarı kaldırır
#gradient de ana resmin kenarları beyaz içi siyah
opening= cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
#resmin üzerinde karartma
tophat = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow("img",img)
cv2.imshow("erosion", erosion)
cv2.imshow("opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()