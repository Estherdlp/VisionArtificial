# -*- coding: utf-8 -*-

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Imagenes/matricula de coches calle.jpg',1)

#Vamos a ecualizar la imagen Gray porque la matricula no tiene detalles a color 
#la imagen a color la llevamos a gray

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_equ = cv.equalizeHist(img_gray)  #solo ecualizamos la luminancia


plt.title('Histograma imagen Original')
plt.hist(img_gray.ravel(), bins=100, range=(0,255))
plt.figure()
plt.title('Histograma imagen ecualizada')
plt.hist(img_equ.ravel(), bins=100, range=(0,255))



plt.figure()
plt.title('Imagen Original')
plt.imshow(img[:,:,::-1])
plt.figure()
plt.title('Imagen en gris ecualizada')
plt.imshow(img_equ, cmap = 'gray') 

