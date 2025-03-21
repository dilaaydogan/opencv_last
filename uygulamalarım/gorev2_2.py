import cv2
import numpy as np

img=cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\input\\para2.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(gray,5)

edges = cv2.Canny(img, 50, 150)

circles = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/32,param1=200,param2=30,minRadius=5,maxRadius=60)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img, (i[0],i[1]), i[2], (0,255,0),2)

if circles is not None:
    print(f"Bulunan daire sayisi: {len(circles[0])}")
else:
    print("Hiç daire bulunamadi.")

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()