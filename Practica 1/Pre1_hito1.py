# -*- coding: utf-8 -*-


"""
#Abrir camara
import cv2 as cv                            #Importar openCV 2 y llamarlo cv
  
####Comprobación de funcionamiento de cámara###
vid = cv.VideoCapture(0)                    #API para capturar frames desde la camara 0
while(True):                                #Bucle infinito de ejecucion (para capturar video)
  ret, frame = vid.read()                   #Captura imagen frame a frame. Devuelve T si ok
  cv.imshow('frame', frame)                 #Muestra los frames en una ventana emergente
                                            #Enmascarar para evitar declaracion implicita del signo en el char.
  if cv.waitKey(1) & 0xFF == ord('q'):      #Dejar de capturar frames si se pulsa q
       break                                #Fin bucle infinito

vid.release()                               #Liberar memoria
cv.destroyAllWindows()                      #Cierra la ventana




#Hacer una foto
import cv2 as cv                            #Importar openCV 2 y llamarlo cv

#### Captura de una imagen  #################
cam = cv.VideoCapture(0)                    #API para capturar frames desde la camara 0
image = cam.read()[1]                       #Guardar valor del frame capturado
cv.imshow("image", image)                   #Mostrar el frame en una ventana emergente
cv.waitKey(0)                               #Esperar hasta que se pulse una tecla
cam.release()                               #Liberar memoria
cv.destroyAllWindows()                      #Cierra la ventana

"""
import cv2 as cv

vid = cv.VideoCapture(0)                    #API para capturar frames desde la camara 0
while(True):                                #Bucle infinito de ejecucion (para capturar video)
  ret, frame = vid.read()                   #Captura imagen frame a frame. Devuelve T si ok
  cv.imshow('frame', frame)                 #Muestra los frames en una ventana emergente
                                            #Enmascarar para evitar declaracion implicita del signo en el char.
  if cv.waitKey(1) & 0xFF == ord('c'):      #Dejar de capturar frames si se pulsa q
      image = vid.read()[1]                 #Guardar el frame en la variable imagen
      break                                 #Fin bucle infinito

vid.release()                               #Liberar memoria
cv.destroyAllWindows()                      #Cerrar ventana

cv.imshow("image", image)                   #Mostrar frame guardado
cv.waitKey(0)                               #Esperar hasta que se pulse una tecla

vid.release()                               #Liberar memoria
cv.destroyAllWindows()                      #Cierra la ventana