import cv2

cv2.namedWindow("klon")
img = cv2.imread("klon.jpg")

#resmin en boy ayarı
img = cv2.resize(img, (640, 480))

cv2.imshow("klon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()