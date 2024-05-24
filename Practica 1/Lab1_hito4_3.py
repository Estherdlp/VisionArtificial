# -*- coding: utf-8 -*-

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#Importar las tres imagenes en escala de grises
img_f1 = cv.imread('Imagenes/Robot_Fondo/F1.jpg',0)
img_f2 = cv.imread('Imagenes/Robot_Fondo/F2.jpg',0)
img_f3 = cv.imread('Imagenes/Robot_Fondo/F3.jpg',0)
#Obtener las dimensiones de las tres imagenes y comprobar las dimensiones
h_1, w_1 = img_f1.shape
h_2, w_2 = img_f2.shape
h_3, w_3 = img_f3.shape
print(h_1 == h_2 == h_3)
print(w_1 == w_2 == w_3)
#Cambiar a 16 bits para evitar desbordamiento
img_f1 = np.uint16(img_f1)
img_f2 = np.uint16(img_f2)
img_f3 = np.uint16(img_f3)
#Generar el promedio de las tres imagenes como una matriz entera con redondeo y cambiar a 8 bits
img_promedio = ((img_f1 + img_f2 + img_f3) / 3)
img_promedio = np.uint8(img_promedio)

#############GENERACION DEL ROBOT SIN FONDO##################
#Sustraer el fondo a las imagenes del robot
#Cargar y representar las dos imagenes con el robot
img_r1 = cv.imread('Imagenes/Robot_Fondo/R1.jpg',0)
#Representar la posicion del robot en escala de grises
plt.figure()
plt.title('Posicion del robot 1')
plt.imshow(img_r1, cmap = 'gray')
#Obtener las dimensiones de las dos imagenes y comprobar las dimensiones
h_4, w_4 = img_r1.shape
print(h_1 == h_4)
print(w_1 == w_4)
#Cambiar formato para evitar desbordes y sustraer la imagen promedio a las imagenes del robot
img_r1 = np.int16(img_r1)
img_promedio = np.int16(img_promedio)
img_robot_1 = abs(img_r1 - img_promedio)
#Cambiar a 8 bits
img_robot_1 = np.uint8(img_robot_1)
img_promedio = np.uint8(img_promedio)
#Representar las imagenes del robot sin fondo
plt.figure()
plt.title('Robot sin fondo 1')
plt.imshow(img_robot_1, cmap = 'gray')

#############OTSU##################
#########################MANUAL##################
B = img_robot_1
histB = cv.calcHist([B], [0], None, [256], [0, 256])
plt.figure()
plt.title('Histograma escala de grises')
plt.plot(histB, color='Blue' )

robot = (B > 65) # el resultado es boolean
plt.figure()
plt.title('Máscara de los núcleos (Manual)')
plt.imshow(robot, cmap='gray')

############# AUTO using OTSU ##########################
#Usando opencv para segmentación por Otsu con thresholding automático
ret1,thresh1 = cv.threshold(B,0,1,cv.THRESH_OTSU)
# ret2,thresh2 = cv.threshold(B,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.figure()
plt.title("Máscara de los núcleos (Otsu-Automático)")
plt.imshow(thresh1,cmap='gray')