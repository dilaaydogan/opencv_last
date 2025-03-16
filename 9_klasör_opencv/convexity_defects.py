#bir şeklin çevresini ve içbükey kusurlarını tespit eder.

import cv2
import numpy as np

img =cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\star.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,0)

contours,_ = cv2.findContours(thresh,2,1)
cnt = contours[0]

hull =cv2.convexHull(cnt, returnPoints = False) #sadece noktaların indeksini alır
defects = cv2.convexityDefects(cnt,hull)  #Şeklin içe bükülen noktalarını (köşelerini) belirler.

#0. elemanı kadar i dönsün
for i in range(defects.shape[0]):
    # start , end , farthest(en uzak nokta, yıldızın içe ükülmüş köşeleri), distance(mesafe)
    s, e, f, d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,255,0],-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()