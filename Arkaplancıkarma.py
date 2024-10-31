import cv2

bg_subtractor = cv2.createBackgroundSubtractorMOG2()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    arkaplan = bg_subtractor.apply(frame)
    cv2.imshow("xc", arkaplan)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
