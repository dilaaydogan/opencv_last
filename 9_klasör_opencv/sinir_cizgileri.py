import cv2

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\contour1.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#gray , min değer , max değer , ya siyah ya beyaz
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#thresh , son iki kontur bulma işleminde varsayılan
contours,ret=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)

