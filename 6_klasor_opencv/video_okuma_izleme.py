import cv2

#capture
cap = cv2.VideoCapture(0)

#ben durduruna kadar video dönsün #frame=kare
while True:
  ret, frame = cap.read()

  #her görüntüyü istediğin eksene göre yansıtır #1 ye eksenine göre
  frame = cv2.flip(frame, 1)
  cv2.imshow("Webcam", frame)
  #karelerin ekranda gözükme süresi
  # / cv2.waitKey(30)
  #q ya basınca pencereyi kapat
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break


#videoyu serbest bırak başka işlem yapabil
cap.release()
cv2.destroyAllWindows()




