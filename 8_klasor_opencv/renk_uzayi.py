import cv2

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\klon.jpg")

#BGR'dan RGB'ye dönüştürme
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #sarımtırak
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #pembemsi
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #gri

cv2.imshow("klon BGR" , img)
cv2.imshow("klon RGB" ,img_rgb)
cv2.imshow("klon HSV" ,img_hsv)
cv2.imshow("klon GRAY" ,img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()