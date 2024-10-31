import cv2

haar_path = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\smile.xml"
path = r"C:\Users\AZAT\Downloads\smile.mp4"
smile_cascade = cv2.CascadeClassifier(haar_path)
cap = cv2.VideoCapture(path)


while 1:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    smiles = smile_cascade.detectMultiScale(gray,1.4,2)
    for x,y,w,h in smiles:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
    cv2.imshow("pence", frame)
    if cv2.waitKey(20) and 0xFF == ord('q'):
        break
cv2.destroyAllWindows()