import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3), np.uint8)
#ad vermemizin sebebi trackbar ara yüzünü bu pencereye yerleştirdiğimizi blirtmek için
cv2.namedWindow("image")


# renk adı , yerleşeceği pencere , başlangıç , bitiş , boş fonk 
cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
#anahtarla aç kapa yapılır
switch = "0: OFF , 1: ON"
cv2.createTrackbar(switch , "image", 0, 1 , nothing)

while True:
    cv2.imshow("image", img)  #güncellenmiş görüntüyü göster
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")


    if s == 0:
       img[:] == [0, 0, 0]  #hiçbir şey değişmez
    if s == 1:
       img[:] = [b, g, r]
       print(s)




cv2.destroyAllWindows()