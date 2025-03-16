import cv2
import numpy as np

#512x512 boyutlarında 3 kanallı (RGB) bir görüntü oluşturur
canvas = np.zeros((512,512,3), dtype=np.uint8)

# başlangıç , bitiş , renk , kalınlık 
cv2.line(canvas, (50,50) , (512,512) , (255,0 ,0), thickness=5) # mavi
cv2.line(canvas, (100,50) , (200,250) , (0,0,250), thickness=7)  #kırmızı

#kalınlık kısmına -1 koyarsan içi dolu olur 
cv2.rectangle(canvas, (20,20) , (50,50) , (0,255,0), thickness=3 )  #yeşil

#merkez , yarıçap , renk , kalınlık
cv2.circle(canvas, (250,250) , 100 , (0,0,255), thickness=-1)

#çokgen her noktası (x,y) formatındca verilir
points = np.array([[[110,200], [330,200], [290,220], [100,100]]], np.int32 )
#birden fazla çizgiyi birleştirme #kapalı şekil olsun diye True dedik
cv2.polylines(canvas, [points], True, (0,0,100),5)


cv2.imshow("Canvas" , canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()