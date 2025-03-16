import cv2
#directshow kamera daha stabil
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fileName = ("C:\opencv.project\video_kaydetme.py\webcam.avi")
#videoların ses ve görüntülerini birleştirmek için algılamayı sağlar
codec =cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
#kare oranı
frameRate = 30
#çözünürlük
resolution = (640, 480)
#video kaydetmek için nesne oluşturur
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

while True:
    ret, frame = cap.read()   #kameradan görüntü oku
    frame = cv2.flip(frame, 1)  # aynalama 
    videoFileOutput.write(frame) #kareyi video dosyasına kaydet
    
    cv2.imshow("webcam", frame)
    # waitkeyin içinde 1 olunca video kendiliğinden devam eder
    if cv2.waitKey(1) & 0xFF == ord("q"):
       break
    
videoFileOutput.release() 
cap.release()
cv2.destroyAllWindows()

