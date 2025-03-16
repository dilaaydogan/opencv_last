import cv2

def nothing(x):   #trackbar'ın hareketi sırasında çağrılan ancak işlem yapmayan bir fonksiyon
    pass

img1 = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\aircraft.jpg")
img1 = cv2.resize(img1,(640,480))

img2  = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\balls.jpg")
img2 = cv2.resize(img2,(640,480))

#ikisinin toplamı 1 olmalı varsayılan olarak da 0 yazılıyo
output = cv2.addWeighted(img1,0.5,img2,0.5,0)

windowName = "Transition Program"
cv2.namedWindow(windowName)

cv2.createTrackbar("Alpha-Beta",windowName,0,1000,nothing) #Alpha-Beta = Trackbar adı

while True:
    cv2.imshow(windowName,output)
    alpha = cv2.getTrackbarPos("Alpha-Beta",windowName)/1000 # trackbar'dan 0 ile 1000 arasında bir değer döndürür.
    beta = 1-alpha
    
    output = cv2.addWeighted(img1,alpha,img2,beta,0)
    print(alpha,beta)
    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()





