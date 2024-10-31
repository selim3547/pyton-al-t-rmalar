import cv2

harcascade_path = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\haarcascade_frontalface_default.xml"


face_casscade = cv2.CascadeClassifier(harcascade_path)
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()

    faces =face_casscade.detectMultiScale(frame,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)

    cv2.imshow("er",frame)

    cv2.waitKey(20)