import cv2

cap = cv2.VideoCapture(0)
path = r"C:\Users\AZAT\Desktop\opencv\mobil_cascade\cascade.xml"
iphone = cv2.CascadeClassifier(path)
while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    mobiles = iphone.detectMultiScale(gray,1.4,4)
    for x,y,w,h in mobiles:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
      cv2.imshow("pence", frame)
    if cv2.waitKey(20) and 0xFF == ord('q'):
          break
cv2.destroyAllWindows()
