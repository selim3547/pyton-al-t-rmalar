import cv2
import numpy as np
path = r"C:\Users\AZAT\Desktop\opencv\resim_okuma_gosterme_kaydetme\klon.jpg"

img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,100,200,3,L2gradient=True)
edges1= cv2.Canny(gray,100,200,3,L2gradient=True)



######################### KONTUR BULMA ################################

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find contours in the grayscale image
konturlar, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, konturlar, -1, (0, 0, 255), 3)
print(konturlar)
cv2.imshow("gray",gray)
cv2.imshow("img",img)

cv2.waitKey(0)

cv2.destroyAllWindows()

