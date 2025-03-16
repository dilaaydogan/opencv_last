#resmin aydınlık karanlık konstrat değerleriyle alakalı grafik 

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = np.zeros((500,500),np.uint8)

cv2.imshow("img", img)

#histogramı çizer 
#img ravel 500,500ü tek satıra döküyo
#kaç değer olduğu
#değer aralığı
plt.hist(img.ravel,256,[0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()