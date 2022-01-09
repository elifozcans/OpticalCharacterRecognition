# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:19:50 2021

@author: ELİF
"""

import pytesseract
import cv2

yol = "C:/Users/EMRE/Desktop/OCR/Ornek2/TcKimlik.png"

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\EMRE\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

resim = cv2.imread(yol)

metin = pytesseract.image_to_string(resim)

print(metin)

cv2.imshow("resim", resim)
cv2.waitKey(0)

