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
#Representar las imagenes en escala de grises
plt.figure()
plt.title('Primer fondo')
plt.imshow(img_f1, cmap = 'gray')
plt.figure()
plt.title('Segundo fondo')
plt.imshow(img_f2, cmap = 'gray')
plt.figure()
plt.title('Tercer fondo')
plt.imshow(img_f3, cmap = 'gray')
plt.figure()
plt.title('Promedio')
plt.imshow(img_promedio, cmap = 'gray')

#Cargar y representar las dos imagenes con el robot
img_r1 = cv.imread('Imagenes/Robot_Fondo/R1.jpg',0)
img_r2 = cv.imread('Imagenes/Robot_Fondo/R2.jpg',0)
#Representar la posicion del robot en escala de grises
plt.figure()
plt.title('Primera posicion')
plt.imshow(img_r1, cmap = 'gray')
plt.figure()
plt.title('Segunda posicion')
plt.imshow(img_r2, cmap = 'gray')
#Obtener las dimensiones de las dos imagenes y comprobar que son iguales
h_4, w_4 = img_r1.shape
h_5, w_5 = img_r2.shape
print(h_1 == h_4 == h_5)
print(w_1 == w_4 == w_5)
#Cambiar formato para evitar desbordes y sustraer la imagen promedio a las imagenes del robot
img_r1 = np.int16(img_r1)
img_r2 = np.int16(img_r2)
img_promedio = np.int16(img_promedio)
img_robot_1 = abs(img_r1 - img_promedio)
img_robot_2 = abs(img_r2 - img_promedio)
#Cambiar a 8 bits
img_robot_1 = np.uint8(img_robot_1)
img_robot_2 = np.uint8(img_robot_2)
img_promedio = np.uint8(img_promedio)
#Representar las imagenes del robot sin fondo
plt.figure()
plt.title('Robot sin fondo 1')
plt.imshow(img_robot_1, cmap = 'gray')
plt.figure()
plt.title('Robot sin fondo 2')
plt.imshow(img_robot_2, cmap = 'gray')


