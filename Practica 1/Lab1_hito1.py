# -*- coding: utf-8 -*-

import cv2 as cv
import matplotlib.pyplot as plt

im = cv.imread('Imagenes/Periquito.bmp')        #Importar periquito a color

#Abrir imagen con OpenCV
cv.imshow("image", im)      #Mostrar imagen
cv.waitKey(0)               #Esperar tecla para poder visualizar la imagen
cv.destroyAllWindows()      #Si se pulsa una tecla, cerrar API visualizacion

#Matplotlib
plt.imshow(im)              #Visualizar con matplotlib la imagen del periquito

#Matplotlib cambiando de BGR a RGB
im_rgb = cv.cvtColor(im, cv.COLOR_BGR2RGB)
plt.figure()                #Crea una nueva figura
plt.imshow(im_rgb)          #Muestra imagen del periquito

#Matplotlib con escala de grises
im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
plt.figure()                #Crea una nueva figura
plt.imshow(im_gray, cmap = 'gray')  #Muestra la imagen con escala de grises
