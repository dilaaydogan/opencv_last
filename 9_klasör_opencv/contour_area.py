import cv2
import os

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\contour.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# görüntü eşik değerinin altındaki pikselleri tamamen siyaha, üstündekileri ise tamamen beyaza çevirmek için kullanılır.
ret, thresh = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY) 
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
# konturları kullanarak alan bulma
area = cv2.contourArea(cnt) 
print(area)
# momentsi kullanarak alan bulma
M = cv2.moments(cnt)
print(M['m00'])

# çevre bulma
perimeter = cv2.arcLength(cnt,True)
print(perimeter)


cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
