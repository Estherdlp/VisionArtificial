# -*- coding: utf-8 -*-

import cv2 as cv

from matplotlib import pyplot as plt
img_bgr = cv.imread('Imagenes/Periquito.bmp')
imB = img_bgr[:,:,0]
imG = img_bgr[:,:,1]
imR = img_bgr[:,:,2]

histB = cv.calcHist([imB], [0], None, [256], [0, 256])
histG = cv.calcHist([imG], [0], None, [256], [0, 256])
histR = cv.calcHist([imR], [0], None, [256], [0, 256])

plt.plot(histB, color='Blue' )
plt.plot(histG, color='Green' )
plt.plot(histR, color='Red' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

plt.figure()                #Crea una nueva figura
plt.title('Canal B')
plt.imshow(imB, cmap = 'gray')          #Muestra imagen del periquito
plt.figure()
plt.title('Canal G')
plt.imshow(imG, cmap = 'gray')
plt.figure()
plt.title('Canal R')
plt.imshow(imR, cmap = 'gray')