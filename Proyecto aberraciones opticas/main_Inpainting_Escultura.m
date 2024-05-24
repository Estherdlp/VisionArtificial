clear all
close all

Imagen = imread('./Imagenes/Escultura.jpg');% Cargar datos (imagenes)
Imagen=im2double(Imagen);
[R,G,B] = imsplit(Imagen);

%% Mascara
%Se hace la trandormada de fourier y se desplaza al centro del arreglo.
R_ft =fftshift(fft2(R));
G_ft =fftshift(fft2(G));
B_ft =fftshift(fft2(B));

Do =21;%Frecuencia de corte.
[N,M] = size(R);%Tamaño delvector.
H = 1-IMG05_GaussianMask(N,M,Do);%Filtro Gauss, paso alto.

%Convolución del filtro.
R_ftc = R_ft.*H;
G_ftc = G_ft.*H;
B_ftc = B_ft.*H;

%Se reordena la tranformada de Fourier.
R_ftt = ifftshift(R_ftc);
G_ftt = ifftshift(G_ftc);
B_ftt = ifftshift(B_ftc);

%transformada inversa de Fourier
R_yo = abs(real(ifft2(R_ftt)));
G_yo = abs(real(ifft2(G_ftt)));
B_yo = abs(real(ifft2(B_ftt)));

%Convolucion de las mascaras
Mascara=((R_yo+G_yo+B_yo)<0.25)


w1=ones(5)/25; % Proporcional a un filtro promedio.
Mascara=imfilter(Mascara,w1);% Se filtra para obtener una mascara mas compacta

lambda=cat(3,Mascara,Mascara,Mascara);% Pasar a RGB la mascara en escala de grises para evitar los problemas de dimensionalidad (triplicar el canal)

%Representacion de todas las mascaras
figure
Graficas=tiledlayout(1,2);
title(Graficas,'Imagen escultura')
nexttile
imshow(Mascara),title('Mascara total');
nexttile
imshow(Imagen), title('Imagen original');
%%
%Se elimina la aberracion cromatica de la imagen
R3=R.*Mascara;
G3=G.*Mascara;
B3=B.*Mascara;

Imgen_nueva=cat(3,R3,G3,B3);%Se crea la nueva imagen a colot

%% Seleccion de parametros -> p = 2
% Proporcionamos los parametros para nuestro algoritmo
varin.lambda    = 100*lambda;   % hyperparametro de fidelidad
varin.Nit       = 2000;         % numero de iteraciones del algoritmo
varin.dt        = 1e-2;         % tamaño del paso 
varin.f         = Imgen_nueva;       % imagen ruidosa
varin.Verbose   = 1;            % Verbose
varin.im_org    = Imgen_nueva;       % Imagen original para el computo de la PSNR
varin.p         = 2;

% Ejecutamos el algoritmo
figure
[varout] = pLap(varin);


% Mostramos el resultado
imagen_inpainting =(varout.u.*(1-Mascara))+Imgen_nueva;



%Representacion del resultado
Graficas=tiledlayout(1,2);
title(Graficas,'Imagen escultura')
nexttile
imshow(Imagen),title('Imagen Original')
nexttile
imshow(imagen_inpainting),title('Imagen inpainting')

print -dpng ./Imagenes/Resultado_Escultura.png