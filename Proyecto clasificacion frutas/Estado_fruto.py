#Importar librerias
import cv2 as cv
import numpy as np

cap = cv.VideoCapture("Tomate.mp4")#Video ("Manzana.mp4") ("Pimiento.mp4")
color="Rojo"#Color "Verde"

width =int(cap.get(cv.CAP_PROP_FRAME_WIDTH))#Anchura del video. 
height =int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))#Altura del video.
fps = cap.get(cv.CAP_PROP_FPS)#Fotogramas por segundos.
#Tipo de archivo para gravar 
fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv.VideoWriter('EstadoFruto.mp4',fourcc, fps, ((width),(height)))

numFrames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))#Número de frame de la imagen.
estado_fruto=np.zeros(numFrames)#Se crea la variable.

for actualFrame in range(numFrames-1):#Se examinan todos los frame
    ret, frame = cap.read()# Se leen los frames.
    if not ret:
        print('No frames')
        break
    
    #Se seleciona el tipo de mascara.
    if color =="Verde":
       imgCanal= frame[:,:,1]
    elif color =="Rojo":  
        imgCanal= frame[:,:,2]
        
    ret,mask = cv.threshold(imgCanal,0,250,cv.THRESH_BINARY+cv.THRESH_OTSU)# Para crear mascara automaticamente.

    kernelApertura = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))# Para el Kernel circular de diámetro 5 píxeles.
    maskConAgujero = cv.morphologyEx(mask, cv.MORPH_OPEN, kernelApertura)# Para la operación morfológica de apertura.

    kernelCierre = cv.getStructuringElement(cv.MORPH_ELLIPSE,(40,40))# Para el Kernel circular de diámetro 40 píxeles.
    mask = cv.morphologyEx(maskConAgujero, cv.MORPH_CLOSE, kernelCierre)# Para la operación morfológica de cierre.
   
    pixeles=np.where(mask==250)#  Para encontrar la posicion de los pixeles blancos.
    filas=np.sort(pixeles[0])# Para segmentar la posicion de los pixeles blancos en fila y ordenarlos.
    columnas=np.sort(pixeles[1])# Para segmentar la posicion de los pixeles blancos en columna y ordenarlos.

    size_filas=round((filas.size-1)*0.13)#Para reducir la reguion de los pixeles blancos (filas).
    filas=np.delete(filas,np.arange(0,size_filas,1))#Reduccion por abajo.
    filas=np.delete(filas,np.arange(filas.max()-size_filas,filas.max(),1)-1)#Reduccion por arriba.

    size_columnas=round((columnas.size-1)*0.23)#Para reducir la reguion de los pixeles blancos (columnas).
    columnas=np.delete(columnas,np.arange(0,size_columnas,1))#Reduccion por abajo.
    columnas=np.delete(columnas,np.arange(columnas.max()-size_columnas,columnas.max(),1)-1)#Reduccion por arriba.

    for n in range(125, 140,10):#Para buscar manchas.
       vector=(0,255,0)#Por defecto
       ret,mask = cv.threshold(imgCanal,n,250,cv.THRESH_BINARY)#Para crea la mascara.
       
       Recorte=np.zeros((filas.max()-filas.min(),columnas.max()-columnas.min()))#Se crea la matriz.
      
       f=np.arange(filas.min(),filas.max(),1)# Se crea el vexctor de filas.
       for c in range (columnas.min(),columnas.max()):#Se reduce la mascara.
          Recorte[f-filas.min(),c-columnas.min()]=mask[f,c]

       if  np.where(Recorte==0)[0].size>10:#Detectan daños.
           if n<130:#Daños severos
             estado_fruto[actualFrame]=2
             vector=(0,0,255)
           else:#Daños leves
               estado_fruto[actualFrame]=1
               vector=(0,255,255)       
           break
       
    cv.rectangle(frame, (columnas.min(),filas.min()), (columnas.max(),filas.max()), vector, 2)# Para dibuja el rectángulo.
    out.write(frame)
       
    
#Estado del fruto    
if np.where(estado_fruto==2)[0].size >6:#Mal estado.
    print('Mal estado del fruto')
elif np.where(estado_fruto==1)[0].size>6:#Estado critico.
     print('Critico estado del fruto ')   
else:#Buen estado
     print('Buen estado del fruto')  

cap.release()#Liberar memoria.
out.release()#Liberar memoria.