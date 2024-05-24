# -*- coding: utf-8 -*-

import cv2 as cv
import os


im = cv.imread('Imagenes/Periquito.bmp')                        #Importar fichero    
h, w, c = im.shape
print('Tipo de dato de cada pixel:', im.dtype)                  #Cada pixel es un byte
print('Tamaño de la imagen: ', h, '*', w, ',', c, 'canales')    #Tamaño imagen alto*ancho*canales
print('Tamaño aproximado, en bytes:', (h*w*c))                  #Peso aproximado imagen
print('Tamaño sin gestion de disco de Windows, en bytes:', os.path.getsize('Imagenes/Periquito.BMP'))         #Peso real imagen
print('La diferencia en bytes entre ambos es:', (os.path.getsize('Imagenes/Periquito.BMP')) - (h*w*c))



cv.imwrite('Imagenes/Periquito.jpg', im)                        #Crear imagen periquito en jpg
cv.imwrite('Imagenes/Periquito_50.jpg', im, [cv.IMWRITE_JPEG_QUALITY, 50])  #Jpg periquito 50% calidad compresion
cv.imwrite('Imagenes/Periquito_25.jpg', im, [cv.IMWRITE_JPEG_QUALITY, 25])  #Jpg periquito 25% calidad compresion


cv.imwrite('Imagenes/Periquito.tiff', im)                       #Crear imagen periquito en tiff


#Compresion https://docs.opencv.org/4.6.0/d8/d6a/group__imgcodecs__flags.html#ga292d81be8d76901bff7988d18d2b42ac
cv.imwrite('Imagenes/Periquito.png', im)                        #Crear imagen periquito en png
cv.imwrite('Imagenes/Periquito_0.png', im, [cv.IMWRITE_PNG_COMPRESSION, 0]) #Sin compresion
cv.imwrite('Imagenes/Periquito_5.png', im, [cv.IMWRITE_PNG_COMPRESSION, 5]) #Compresion media (rango 0 - 9)