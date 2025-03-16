import cv2 
import numpy as np

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\klon.jpg")

#resmin boyutlarını ve kanal değerini verir
dimension = img.shape


#koordinatlardaki renk değerini verir
color = img[150,200]
print("BGR", color)


blue = img[420,500,0]
print("blue:", blue)


green = img[420,500,1]
print("green:", green)


red = img[420,500,2]
print("red:",red)

#pikseli değiştirmek için 
img[420,500,0] = 250
print("new blue:", img[420,500,0])

#pikseli değiştirmek için farklı bir yöntem
blue1 = img.item(150,200,0)
print("blue1:", blue1)

img.itemset((150,200,0), 172)
print("new blue1:", img[150,200,0])



cv2.imshow("klon Asker" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()