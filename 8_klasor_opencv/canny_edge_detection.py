import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
#flip görüntüyü takla attır
    frame = cv2.flip(frame,1) #1=ayna yatay eksen

#edges = kenarlar 
    edges = cv2.Canny(frame,100,200)

    cv2.imshow("Frame",frame)
    cv2.imshow("Edges",edges)

    if cv2.waitKey(5) & 0xFF==ord('q'):  #cv2.waitKey(5): 5 milisaniye boyunca klavyeden bir tuş girişini bekler.
        break

cap.release()
cv2.destroyAllWindows()
    
