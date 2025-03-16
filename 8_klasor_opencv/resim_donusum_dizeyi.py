#öteleme yapar

import cv2
import numpy as np


#0 yazınca siyah beyaz oldu
img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\klon.jpg",0)
#row  satır col sütun
row,col = img.shape

# 200 değeri soldan uzaklık 70 üstten uzaklık
M = np.float32([[1,0,200],[0,1,70]])

#warpAffine ile resmi istediğimiz gibi kaydırdır
dst = cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()