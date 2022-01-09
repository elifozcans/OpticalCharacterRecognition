# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:16:40 2021

@author: ELIF OZCAN
"""

#Python-tesseract is an optical character recognition (OCR) tool for python.
#That is, it will recognize and “read” the text embedded in images.


import cv2
import pytesseract
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\EMRE\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
#tesseract_cmd = r'C:\Users\EMRE\AppData\Local\Programs\Tesseract-OCR'

img = cv2.imread("deneme.jpg")
#Alternatively: can be skipped if you have a Blackwhite image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
out_below = pytesseract.image_to_string(Image.open('deneme.jpg'), lang="tur")

print("OUTPUT:", out_below)

out_below

