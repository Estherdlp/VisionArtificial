# -*- coding: utf-8 -*-

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

im = cv.imread('Imagenes/Periquito.bmp')        #Importar periquito a color

im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
cv.imwrite('Imagenes/Periquito_gray.bmp', im_gray)



im_2 = cv.imread('Imagenes/Periquito_gray.bmp')
cv.imshow("image", im_2)    #Mostrar imagen
cv.waitKey(0)               #Esperar tecla para poder visualizar la imagen
cv.destroyAllWindows()      #Si se pulsa una tecla, cerrar API visualizacion
h, w, c = im_2.shape
print('Numero de canales:', c)    #Numero de canales
print(np.array_equal(im_2[:,:,0], im_2[:,:,1]))
print(np.array_equal(im_2[:,:,0], im_2[:,:,2]))



im3 = cv.imread('Imagenes/Periquito.bmp',0)
cv.imshow("image", im3)    #Mostrar imagen
cv.waitKey(0)               #Esperar tecla para poder visualizar la imagen
cv.destroyAllWindows()      #Si se pulsa una tecla, cerrar API visualizacion
print(im3.shape)