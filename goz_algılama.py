import cv2
path = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\eyehaascade.xml"
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(path)

while 1:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
    if cv2.waitKey(20) and 0xFF == ord("q"):
        break


    cv2.imshow("ds",frame)
cv2.destroyAllWindows()