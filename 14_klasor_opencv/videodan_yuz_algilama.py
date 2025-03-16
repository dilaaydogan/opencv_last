import cv2   


vid = cv2.VideoCapture("C:\\Users\\dila\\Desktop\\opencv.project\\input\\faces.mp4")
face_cascade = cv2.CascadeClassifier("C:\\Users\\dila\\Desktop\\cascade\\haarcascade_faces.xml")

while 1:
    
    # frameleri tek tek okur
    ret, frame = vid.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # yüzlerin koordinarlarını bul
    faces = face_cascade.detectMultiScale(gray, 1.1, 2)

    #yüzleri dikdörtgen içerisine al
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow('video',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()