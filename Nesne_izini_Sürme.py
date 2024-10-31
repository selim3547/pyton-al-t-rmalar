import cv2
import numpy as np

path = r"C:\Users\AZAT\Desktop\opencv\line.mp4"
cap = cv2.VideoCapture(path)

while True:
    ret,frame = cap.read()
    if not ret:
      break

    frame = cv2.resize(frame, (640,600))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Renk uzayını HSV'ye çevir

    lower_yellow = np.array([18, 94,  140], np.uint8)
    upper_yellow = np.array([48, 255, 255], np.uint8)

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    cv2.imshow("Mask", mask)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
