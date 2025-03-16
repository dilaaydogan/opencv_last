import cv2
import numpy as np

img_filter = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\filter.png")
img_median = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\median.png")
img_bilateral = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\bilteral.png")

blur =cv2.blur(img_filter,(5,5))
blur_f=cv2.filterBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median,5)
blur_b = cv2.bilateralFilter(img_bilateral,9,95,95)

cv2.imshow("original",img_filter)
cv2.imshow("blur",blur)


cv2.waitKey(0)
cv2.destroyAllWindows()