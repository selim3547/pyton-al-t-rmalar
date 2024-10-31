import cv2

path = r"C:\Users\AZAT\Desktop\opencv\car.mp4"
path_haar = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\car.xml"
img1 = cv2.imread(path)
cap = cv2.VideoCapture(path)
car_cascade = cv2.CascadeClassifier(path_haar)



while 1:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.4, 2)
    for x,y,w,h in cars:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)


    cv2.imshow("pence",frame)
    if cv2.waitKey(20) and 0xFF == ord('q'):
        break



cv2.destroyAllWindows()