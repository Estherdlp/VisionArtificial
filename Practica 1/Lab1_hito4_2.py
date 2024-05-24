# -*- coding: utf-8 -*-

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Imagenes/Robot_Fondo/R3.jpg',0)
plt.figure()
plt.title("Original")
plt.imshow(img, cmap = 'gray')

#########################MANUAL##################
B = img
histB = cv.calcHist([B], [0], None, [256], [0, 256])
plt.figure()
plt.title('Histograma escala de grises')
plt.plot(histB, color='Blue' )


robot = (B < 78) # el resultado es boolean
plt.figure()
plt.title('Máscara de los núcleos (Manual)')
plt.imshow(robot, cmap='gray')

############# AUTO using OTSU ##########################
#Usando opencv para segmentación por Otsu con thresholding automático
# ret2,thresh2 = cv.threshold(B,0,1,cv.THRESH_BINARY_INV)
ret2,thresh2 = cv.threshold(B,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
plt.figure()
plt.title("Máscara de los núcleos (Otsu-Automático)")
plt.imshow(thresh2,cmap='gray')


#INVERTIR RESULTADO PARA QUE EL ROBOT SE VEA BLANCO Y EL FONDO NEGRO