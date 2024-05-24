#Declaración de librerías.
import numpy as np
import cv2 as cv


cap = cv.VideoCapture("Robot.mp4")#API para abrir el video del robot.
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))#Anchura del video. 
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))#Altura del video.
fps = cap.get(cv.CAP_PROP_FPS)#Fotogramas por segundos.
#Tipo de archivo para gravar. 
fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv.VideoWriter('outputRobot.mp4',fourcc, fps, (width, height))

# Crea ventana centrada en el centro del monitor.
windowName = 'Esquinas detectadas'
cv.namedWindow(windowName, cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty(windowName,cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
(_,_,screenWidth,screenHeight) = cv.getWindowImageRect(windowName)
cv.setWindowProperty(windowName,cv.WND_PROP_FULLSCREEN,cv.WINDOW_NORMAL)
windowWidth = int(width/2)
windowHeight = int(height/2)
cv.moveWindow(windowName, int(screenWidth/2-windowWidth/2), int(screenHeight/2-windowHeight/2))
cv.resizeWindow(windowName, windowWidth, windowHeight)   

ret, frame = cap.read()#Guarda el primer frame.
oldFrameGris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #Primer frame en escala de grises.

#Obtiene las esquinas más pronunciadas con el método de Shi-Tomasi.
maxCorners = 70
qualityLevel = 0.4
minDistance = 40
esquinasOldFrame = cv.goodFeaturesToTrack(oldFrameGris, maxCorners, qualityLevel, minDistance);

# Visualiza las esquinas detectadas.
for ind in range(len(esquinasOldFrame)):
    esquinas = cv.circle(frame, (int(esquinasOldFrame[ind,0][0]),int(esquinasOldFrame[ind,0][1])), 10, (0,0,255), -1)
cv.imshow(windowName, esquinas)
cv.waitKey(0)

imagenEstela = np.zeros_like(frame)#Variable imagenEstela con el mismo tamaño que frame.
color = np.random.randint(0, 255, (70, 3))#70 colores RGB aleatorios.

while(1):#Para el resto de frames.
    
    ret, frame = cap.read()# Se leen los frames.
    if not ret:
        print('No frames')
        break
    
    newFrameGris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)#Frame a escala de grises.
    esquinasNewFrame, estado, error = cv.calcOpticalFlowPyrLK(oldFrameGris, newFrameGris, esquinasOldFrame, None,  maxLevel = 2)#Lucas-Kanade. 
    
    if esquinasNewFrame is not None:#Selecionan las nuevas esquinas.
        esquinasNewFrameDetect = esquinasNewFrame[estado==1].reshape(-1, 1, 2)
        esquinasOldFrameDetect = esquinasOldFrame[estado==1].reshape(-1, 1, 2)
               
    for ind in range(len(esquinasNewFrameDetect)):#Dibuja las estelas.
        coordNew = np.int16(esquinasNewFrameDetect[ind][0])
        coordOld = np.int16(esquinasOldFrameDetect[ind][0])
        imagenEstela = cv.line(imagenEstela, (coordNew[0], coordNew[1]), (coordOld[0], coordOld[1]), color[ind].tolist(), 5)
        frame = cv.circle(frame,(int(width/2), int(height/2)), 10, color[ind].tolist(), -1)#Punto en el centro.
    extIndices = np.where(np.logical_or(imagenEstela[:,:,0] != 0, imagenEstela[:,:,1] != 0, imagenEstela[:,:,2] != 0))#Localiza los puntos de la estela.
    frame[extIndices[0],extIndices[1],:] = imagenEstela[extIndices[0],extIndices[1],:]#Introduce la estela en el frame.

    cv.imshow(windowName, frame)#Muestra el frame.
    out.write(frame)#Graba el frame.
    
    #Nuevos valores para la siguiente iteración.  
    oldFrameGris = newFrameGris
    esquinasOldFrame = esquinasNewFrame
    
    k = cv.waitKey(1)#Se pulsa Esc.
    if k == 27:#Se sale.
        break

cap.release()#Liberar memoria.
out.release()#Liberar memoria.
cv.destroyAllWindows()#Cierra la ventana.
