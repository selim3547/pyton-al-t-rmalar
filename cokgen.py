import cv2
import numpy as np



cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        epsilon = 0.03 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if len(approx) >= 3 and len(approx) <= 6:
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
        if len(approx) == 4:
            cv2.putText(frame, "kare", (x, y), font, 1, 0)
        elif len(approx) == 5:
            cv2.putText(frame, "beşgen", (x, y), font, 1, 0)
        elif len(approx) == 6:
            cv2.putText(frame, "altıgen", (x, y), font, 1, 0)
    cv2.imshow('Polygon Detection', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
