import tesseract
import cv
import cv2
import numpy as np
import pyttsx
from win32com.client import constants, Dispatch
img = cv2.imread('C:/Python27/progg/pic/godisgreat.jpg')
retval, threshold = cv2.threshold(img,50, 126,cv2.THRESH_BINARY)


grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled,50, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 15)

offset=50
height,width = gaus.shape
gaus=cv2.copyMakeBorder(gaus,offset,offset,offset,offset,cv2.BORDER_CONSTANT,value=(255,255,255)) 
#cv2.namedWindow("Test")
#cv2.imshow("Test", gaus)
cv2.imwrite("an91cut_decoded.jpg",gaus)

### tesseract OCR
api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)
height1,width1 = gaus.shape
channel1=1
image = cv.CreateImageHeader((width1,height1), cv2.IPL_DEPTH_8U, channel1)
cv.SetData(image, gaus.tostring(),gaus.dtype.itemsize * channel1 * (width1))
tesseract.SetCvImage(image,api)
tex=api.GetUTF8Text()
conf=api.MeanTextConf()
g=open('god.txt' , 'w')
g.write(tex)
g.close()
g = open("god.txt")
thegod=g.read()
with open("god.txt", "r") as f:
    for line in f:
        cleanedLine = line.strip()
        if cleanedLine: # is not empty
            print(cleanedLine)
speaker = Dispatch("SAPI.SpVoice")  #Create SAPI SpVoice Object
speaker.Speak(tex)#Process TTS

del speaker 
