from PIL import Image
import pytesseract
import cv2
import cv
img= cv2.imread('C:/Python27/progg/pic/webcam/close.jpg')
tex = pytesseract.image_to_string(Image.open('C:/Python27/progg/pic/webcam/close.jpg'), lang='tam')# Assign output data to varibale for passing as parameter for any application
print(pytesseract.image_to_string(Image.open('C:/Python27/progg/pic/webcam/close.jpg'), lang='eng'))
cv2.namedWindow("Input image")
cv2.imshow("Input image",img)
cv2.waitKey(0)
cv2.destroyWindow("Test")
cv2.destroyWindow("Main")
