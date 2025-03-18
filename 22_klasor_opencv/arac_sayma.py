
import cv2
import numpy as np

vid = cv2.VideoCapture("C:\\Users\\dila\\Desktop\\opencv.project\\input\\traffic.avi")
backsub = cv2.createBackgroundSubtractorMOG2()  #MOG2 Algoritması kullanılarak arka plan çıkarılır
c = 0 # sayaç
while True:
    ret,frame = vid.read()
    if ret:
        fgmask = backsub.apply(frame) #arka planı çıkar ön plan kalsın
        cv2.line(frame,(50,0),(50,300),(0,255,0),2) #başlangıç , bitiş , renk , kalınlık
        cv2.line(frame,(70,0),(70,300),(0,255,0),2)
        #cv2.CHAIN_APPROX_SIMPLE: Konturları optimize eder, gereksiz noktaları kaldırır.
        contours,hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # hierarchy resim topolojisiyle alakalı bilgiler tutar
        try : hierarchy = hierarchy[0]
        except: hierarchy=[]
        #cv2.boundingRect(contour): Konturu saran dikdörtgenin koordinatlarını ve boyutlarını (x, y, w, h) alır.
        for contour,hier in zip(contours,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w>40 and h >40: #Sadece belirli bir genişlik (w) ve yükseklik (h) e sahip nesneler seçilir.
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                if x>50 and x<70:  #Eğer aracın x koordinatı 50 ile 70 arasındaysa, c sayacı 1 artırılır.
                    c+=1

         #cv2.putText() fonksiyonu, görüntünün üstüne kırmızı renkte araç sayısını yazar.       
        cv2.putText(frame,"car: "+str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
        

        cv2.imshow("Car Counter",frame)
        cv2.imshow("Fgmask",fgmask)
        
        if cv2.waitKey(40) & 0xFF==ord('q'):
            break

vid.release()
cv2.destroyAllWindows()      