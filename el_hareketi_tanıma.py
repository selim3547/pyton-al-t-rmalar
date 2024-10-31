import cv2

path = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\handcascade.xml"
hand_cascade = cv2.CascadeClassifier(path)

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(frame_gray,1.1,20)
    for x,y,w,h in hands:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("des",frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()