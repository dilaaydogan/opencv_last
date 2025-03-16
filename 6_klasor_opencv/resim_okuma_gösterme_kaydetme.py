import cv2

#resmi okuma  #0 yazarsan gri okur
img = cv2.imread("klon.jpg", 0)
# print(img)
#pencere oluşturma
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
#resmi görme
cv2.imshow("image" , img)
#resmi kaydetme
cv2.imwrite("klon1.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()