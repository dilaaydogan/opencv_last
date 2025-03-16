import cv2
import numpy as np

image_path = ("C:\\Users\\dila\\Desktop\\opencv.project\\input\\starwars.jpg")
template_path = ("C:\\Users\\dila\\Desktop\\opencv.project\\input\\starwars2.jpg")

img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread(template_path,cv2.IMREAD_GRAYSCALE)
#template.shape → Şablonun (yükseklik, genişlik) değerlerini döndürür.
#[::-1] ile ters çevrildiğinde (genişlik, yükseklik) sırasına getirilir.
w,h = template.shape[::-1] 

#cv2.TM_CCOEFF_NORMED → En iyi eşleşmeyi -1 ile 1 arasında normalize eder (1 en iyi eşleşme).
result = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)
location = np.where(result >= 0.95) #np.where(result >= 0.95) → Eşleşme değeri %95'ten büyük olan (0.95 ve üzeri) bölgeleri bulur.

#yükseklik ve genişlik alıyo -1 yazınca wh yerine hw
for point in zip(*location[::-1]):
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,0),3) #üst sol köşe , alt sağ köşe , renk , kalınlık


cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()