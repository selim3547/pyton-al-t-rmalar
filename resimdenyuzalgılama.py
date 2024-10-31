import cv2

image_path = r"C:\Users\AZAT\Desktop\opencv\opencv_udemy\basketball-95607_640.jpg"
yol = r"C:\Users\AZAT\Desktop\opencv\haar_cascade\fronandallfacepeople.xml"
face_cascade = cv2.CascadeClassifier(yol)

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 7)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255))

cv2.imshow("img", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
