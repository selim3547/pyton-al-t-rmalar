import cv2
from PIL import Image
import pytesseract
path = r"C:\Users\AZAT\Desktop\opencv\opencv_udemy\800px-OpenCV_Logo_with_text_svg_version.svg.png"
img = Image.open(path)

text = pytesseract.image_to_string(img,lang="eng")
print(text)