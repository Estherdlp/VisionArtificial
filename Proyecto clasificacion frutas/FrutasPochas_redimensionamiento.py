# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:41:07 2023

@author: Esther
"""
import glob
import cv2 as cv

#Redimensionar las imagenes a 32x32x3
files = glob.glob(r"fruits-360_dataset\fruits-360\**\**\*.jpg", recursive=True)
print(len(files))
for file in files:
  image = cv.imread(file)
  image_resized = cv.resize(image, (32, 32))
  cv.imwrite(file, image_resized)