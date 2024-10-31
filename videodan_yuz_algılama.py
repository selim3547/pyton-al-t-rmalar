import cv2

cap = cv2.VideoCapture(0)
yol = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\fronandallfacepeople.xml"
face_cascade = cv2.CascadeClassifier(yol)

while 1 :
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,4)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(w+x,y+h),(0,255,0),4)


    if cv2.waitKey(50) and 0xFF == ord('q'):
        break
    cv2.imshow("sdlk", frame)