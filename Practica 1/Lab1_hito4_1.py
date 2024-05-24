# -*- coding: utf-8 -*-

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Imagenes/Osteosarcoma_01.tif", 1)
plt.figure()
plt.title("Original")
img_rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img_rgb)

#########################MANUAL##################
#Separa canal azul porque contiene los pixeles de los núcleos 
B = img[:,:,0]
plt.figure()
plt.title("Original-Canal Blue")
plt.imshow(B, cmap='gray')

# Umbralización Manual 
nucleos = (B > 40) # el resultado es boolean
plt.figure()
plt.title("Máscara de los núcleos (Manual)")
plt.imshow(nucleos, cmap='gray')

#Lo mismo pero Usando opencv para hacer un manual threshold
#Los pixels mayores que 40 se fuerzan a 1
ret1, thresh1 = cv.threshold(B, 40, 1, cv.THRESH_BINARY)
plt.figure()
plt.title("Máscara de los núcleos (OpenCV-Manual)")
plt.imshow(thresh1, cmap='gray')

############# AUTO using OTSU ##########################
#Usando opencv para segmentación por Otsu con thresholding automático
ret2,thresh2 = cv.threshold(B,0,1,cv.THRESH_OTSU)
# ret2,thresh2 = cv.threshold(B,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.figure()
plt.title("Máscara de los núcleos (Otsu-Automático)")
plt.imshow(thresh2,cmap='gray')

