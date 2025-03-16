
import cv2   

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\eye.png")

face_cascade = cv2.CascadeClassifier("C:\\Users\\dila\\Desktop\\face.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\dila\\Desktop\\haarcascade_eye.xml")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
# her bir kare üzerindeki yüzlerin koordinarlarını bul
faces = face_cascade.detectMultiScale(gray,1.4,5)
print("kaç tane:" , len(faces))

# tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alırız
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3) 
    
    gray2 = gray[y:y+h, x:x+w] 
    img2 = img[y:y+h, x:x+w] 
    eyes = eye_cascade.detectMultiScale(gray,1.5,3) 
    
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
         

cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()