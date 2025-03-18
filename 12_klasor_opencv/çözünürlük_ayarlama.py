import cv2

windowName = "Live Video"
cv2.namedWindow(windowName)

cap = cv2.VideoCapture(0)

#3 yazınca eni verir 4 yazınca yükseklik verir
print("Width : "+str(cap.get(3)))
print("Height : "+str(cap.get(4)))

cap.set(3,1280) # Görüntü genişliğini 1280 piksele ayarlar.
cap.set(4,720) # Görüntü yüksekliğini 720 piksele ayarlar.

#Yıldız (*) işareti, çözünürlüğün değiştiğini göstermek için eklenmiş
print("Width* : "+str(cap.get(3)))
print("Height* : "+str(cap.get(4)))

while True:
    _,frame = cap.read()
    frame = cv2.flip(frame,1) #Görüntüyü yatay olarak çevirir (ayna efekti verir).

    cv2.imshow(windowName,frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

    