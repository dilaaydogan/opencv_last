import cv2 
import numpy as np


#boş tuval oluşturma
circle = np.zeros((512, 512, 3), np.uint8) +255
# çember , merkez konumu , yarıçap , renk , içi dolu 
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)
#boş tuval oluşturma
rectangle = np.zeros((512, 512, 3), np.uint8) +255
# dikdörtgen , başlangıç , bitiş , renk , içi dolu
cv2.rectangle(rectangle, (150,150), (350,350), (0,0,255), -1 )

add = cv2.add(circle, rectangle)
print(add[256,256])


cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("add", add)

cv2.waitKey(0)
cv2.destroyAllWindows()