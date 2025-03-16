import cv2 
import numpy as np

#canvas=tuval 
#belli bi alana siyah tuval oluşturmak
#çizim yapıldığında kullanılan veri tipi np.uint8
# +() başka sayı yazarsan ekranın rengi değişir
canvas = np.zeros((512, 512, 3), dtype=np.uint8) +100

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

