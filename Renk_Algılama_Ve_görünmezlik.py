import cv2

cap = cv2.VideoCapture(0)



path = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(path)

while 1:
    ref,frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray,1.1,3)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow("esd",frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()