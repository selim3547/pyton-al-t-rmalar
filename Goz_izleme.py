import cv2

path1 = r"C:\Users\AZAT\Desktop\opencv\bitwise_1.png"
path2 = r"C:\Users\AZAT\Desktop\opencv\bitwise_2.png"
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

if (img1 == img2).all():
    print("Görüntüler aynı")
else:
    print("Görüntüler farklı")

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
