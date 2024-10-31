import cv2
import numpy as np
path = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\fronandallfacepeople.xml"
canvas = np.zeros((500,500),dtype=np.uint8)
face_cascade = cv2.CascadeClassifier(path)
cap = cv2.VideoCapture(0)
face_list = []
while True:
    _,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame,1.2,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),4)
        face_list.append((x,y,w,h))

    cv2.imshow("sd",frame)
    for x, y, w, h in face_list:
        cv2.rectangle(canvas, (x, y), (x + w, y + h),(255,0,0),4)

    cv2.imshow("dsa", canvas)
    if cv2.waitKey(20) & 0xFF == ord('x'):
        break

