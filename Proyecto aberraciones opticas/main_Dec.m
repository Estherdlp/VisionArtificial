%% -----------------Fundamentos Matem???ticos - MOVA 2018----------------- %%
%                        Pr???ctica 2  - Deconvolution                      %
% I. Ramirez, E. Schiavi                                                  %
% URJC - Madrid 2018                                                      %
%%-----------------------------------------------------------------------%%


%% Cargar datos (im???genes)
clear all, close all, clc
imagen = imread('./Imagenes/curvatura.png'); 
imagen = im2double(imagen);

%% Selecci???n de par???metros p = 2
% Definir el filtro de difusión lineal para corregir la aberración de curvatura de campo
kernel = fspecial('disk', 1);                   % Radio del filtro: 1
dim = size(imagen);
kernel_F = psf2otf(kernel,[dim(1),dim(2)]);

% Proporcionamos los parametros para nuestro algoritmo
varin.lambda    = 1000;         % hyperpar?ametro de fidelidad
varin.Nit       = 3;            % numero de iteraciones del algoritmo
varin.dt        = 1e-2;         % tamaño del paso 
varin.f         = imagen;       % imagen ruidosa (la imagen original ya tiene ruido)
varin.Verbose   = 1;            % Verbose
varin.im_org    = imagen;       % Imagen original para el c???mputo de la PSNR
varin.p         = 2;
varin.kernel    = kernel;
varin.kernel_F  = kernel_F;

% Ejecutamos el algoritmo
[varout] = pLap_Deconvolution(varin);

% Mostramos el resultado
u2 = varout.u;

%% Comparacion con metodos de matlab
close all
[u_matlab, LAGRA] = deconvreg(imagen,kernel,[],2);

figure, 
subplot(221), imshow(imagen),   title('Original')
subplot(222), imshow(u_matlab), title('Deconvolucion calculada por matlab')
subplot(223), imshow(u2),       title('Deconvolucion algoritmo clase')
%% Bordes de la imagen
BW = edge(rgb2gray(imagen),'Canny');
figure, imshow(BW), title('Original')

BW_post = edge(rgb2gray(u2),'Canny');
figure, imshow(BW_post), title('Bordes deconvolución')
