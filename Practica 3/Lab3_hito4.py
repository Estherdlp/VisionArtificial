#Declaración de librerías.
import numpy as np
import cv2 as cv
import numpy as np
import math as ma


#Decalración de funciones.
def suavizar(trayectoria):  
    radio = 50
    tamVentana = 2 * radio + 1
    filtro = np.ones(tamVentana)/tamVentana 

    trayectoriaSuavizada = np.copy(trayectoria)
    for i in range(3):
        curvaPad = np.lib.pad(trayectoria[:,i], (radio, radio), 'edge') 
        curvaSuavizadaPad = np.convolve(curvaPad, filtro, mode='same') 
        trayectoriaSuavizada[:,i] = curvaSuavizadaPad[radio:-radio]
    return trayectoriaSuavizada

cap = cv.VideoCapture("RobotFijo.mp4")#API para abrir el video del robot.
width =int(cap.get(cv.CAP_PROP_FRAME_WIDTH))#Anchura del video. 
height =int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))#Altura del video.
fps = cap.get(cv.CAP_PROP_FPS)#Fotogramas por segundos.
#Tipo de archivo para gravar 
fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv.VideoWriter('outputRobotFijo.mp4',fourcc, fps, ((2*width),(height)))

# Crea ventana centrada en el centro del monitor
windowName = 'Video'
cv.namedWindow(windowName, cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty(windowName,cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
(_,_,screenWidth,screenHeight) = cv.getWindowImageRect(windowName)
cv.setWindowProperty(windowName,cv.WND_PROP_FULLSCREEN,cv.WINDOW_NORMAL)
windowWidth = int(width/2)
windowHeight = int(height/2)
cv.moveWindow(windowName, int(screenWidth/2-windowWidth/2), int(screenHeight/2-windowHeight/2))
cv.resizeWindow(windowName, windowWidth, windowHeight)

ret, frame = cap.read()#Primer frame.
oldFrameGris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)#Primer frame en escala de grises.

numFrames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))#Número de frame de la imagen.
movimientos = np.zeros((numFrames-1, 3), np.float32) #Declaración del vector de movimientos.
T=np.zeros((2,3))#Declaración del vector T (Transformaciones).

while(1):
    
   for actualFrame in range(numFrames-1):#Para el resto de frames.
    ret, frame = cap.read()# Se leen los frames.
    if not ret:
        print('No frames')
        break
    
    newFrameGris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)#Frame a escala de grises.
    
    #Obtiene las esquinas más pronunciadas con el método de Shi-Tomasi.
    maxCorners = 70
    qualityLevel = 0.4
    minDistance = 40
    esquinasOldFrame = cv.goodFeaturesToTrack(oldFrameGris, maxCorners, qualityLevel, minDistance);
    esquinasNewFrame, estado, error = cv.calcOpticalFlowPyrLK(oldFrameGris, newFrameGris, esquinasOldFrame, None,  maxLevel = 1)#Lucas-Kanade.

    movimientos1 =cv.estimateAffinePartial2D(esquinasOldFrame,esquinasNewFrame)[0]#Transformación des un frame al otro.
    
    if movimientos1 is not None:#Si hay movimiento.
     x=movimientos1[0]
     y=movimientos1[1]
     s=ma.sqrt(y[0]**2+y[1]**2)#Escalado
     movimientos[actualFrame,2]=np.arcsin(y[0]/s)#Angulo de giro
     movimientos[actualFrame,1]=y[2]#Y
     movimientos[actualFrame,0]=x[2]#X
    oldFrameGris = newFrameGris

    k = cv.waitKey(1)#Se pulsa Esc.
    if k == 27:#Se sale.
     break
 
   cap = cv.VideoCapture("RobotFijo.mp4")#Se vuelve a cargar la imagen.
   
   #Correccion de movimiento.
   trayectoria = np.cumsum(movimientos, axis=0) 
   trayectoriaSuavizada=suavizar(trayectoria)
   ajustes = trayectoriaSuavizada - trayectoria
   movimientosSuavizados = movimientos + ajustes
   
   for actualFrame in range(numFrames-1):#Para el resto de frames.
        ret, frame = cap.read()
        if not ret:
            print('No frames')
            break
        #Se crea la matriz de transformación T 
        T[0,0]=np.cos(movimientosSuavizados[actualFrame,2])#cos(Rotacion)
        T[0,1]=-np.sin(movimientosSuavizados[actualFrame,2])#-sen(Rotacion)
        T[0,2]=movimientosSuavizados[actualFrame,0]#X
    
        T[1,0]=np.sin(movimientosSuavizados[actualFrame,2])#sen(Rotación)
        T[1,1]=np.cos(movimientosSuavizados[actualFrame,2])#cos(Rotación)
        T[1,2]=movimientosSuavizados[actualFrame,1]#Y
        
        frameEstabilizado = cv.warpAffine(frame, T, (width,height))
        
        escalado = cv.getRotationMatrix2D((width/2,height/2), 0, 1.20)
        frameEstabilizadoEscalado = cv.warpAffine(frameEstabilizado, escalado, (width,height))
        frameComp = cv.hconcat([frameEstabilizado,frameEstabilizadoEscalado])#Frame estabilizado y sin estabilizar en un frame partido.
        
        cv.imshow(windowName,frameComp)
        out.write(frameComp)#Graba.
    
        k = cv.waitKey(1)#Se pulsa Esc.
        if k == 27:#Se sale.
          break

   break

cap.release()#Liberar memoria
out.release()#Liberar memoria
cv.destroyAllWindows()#Cierra la ventana

