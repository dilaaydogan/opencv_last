import cv2

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\starwars.jpg")
blurry_img = cv2.medianBlur(img,9)  #9 → Filtre boyutudur (9x9 piksel). Daha büyük değerler daha fazla bulanıklık oluşturur.

#9 → Filtre boyutudur (9x9 piksel). Daha büyük değerler daha fazla bulanıklık oluşturur.
laplacian= cv2.Laplacian(blurry_img,cv2.CV_64F).var()
print(laplacian) #cv2.Laplacian() fonksiyonu, görüntünün kenar keskinliğini hesaplar.

if laplacian < 500: #Eğer Laplacian varyansı 500'den küçükse, görüntü bulanık kabul edilir.

    print("blurry image")


cv2.imshow("img",img)
cv2.imshow("blurry_img",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
