import cv2
import numpy as np
path = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\eyehaascade.xml"
cap = cv2.VideoCapture(0)
face_cascade= cv2.CascadeClassifier(path)
face = []
while True:
    ref,frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame_gray,1.1,5)
    

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
        face.append(x,y,w,h)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Devam Kontrolu', frame)
cap.release()
cv2.destroyAllWindows()