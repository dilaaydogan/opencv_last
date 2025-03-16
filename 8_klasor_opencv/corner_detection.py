
import cv2
import numpy as np


img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\text.png")
img1 = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\contour.png")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#işleme sokulması için float tipine çevirdik
gray = np.float32(gray)

#gray , köşe sayısı ,kalite değeri , köşeler arası min mesafe
corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)

#çemberlerde float sayı kullanılmaz o yüzden inte geri çevirdik
corners = np.int32(corners)
#ccornerin içindeki değerleri çeksin diye
for corner in corners:
# tek bir satıra dökmek için
    x,y = corner.ravel()
#img değişkeni, x-y merkez, yarıçap, renk, içi dolu daire
    cv2.circle(img,(x,y),3,(0,0,255),-1)

cv2.imshow("corner",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

  