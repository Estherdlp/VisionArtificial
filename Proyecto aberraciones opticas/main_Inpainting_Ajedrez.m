clear all
close all

imagen = imread('./Imagenes/Ajedrez.jpg'); % Cargar datos (imagenes)
% Convertir la imagen a tipo de datos de punto flotante para realizar cálculos
imagen = im2double(imagen);

% Separar los canales de la imagen y transformar los datos en tipo double y en el rango [0,1].
imagen = im2double(imagen);
[canalRojo,canalVerde,canalAzul] = imsplit(imagen);

%% Calculo de las mascaras para las aberraciones
mask_verde = imagen - canalAzul - canalRojo;
mask_magenta = imagen - canalVerde - 0.4.*canalAzul;

mask_verde_mod=(mask_verde(:,:,2)>= -0.05);
mask_magenta_mod=((mask_magenta(:,:, 1) >= 0)+(mask_magenta(:, :, 3) >= 0.1))>0;

%Juntar ambas mascaras en una unica
mask =1-(mask_verde_mod+mask_magenta_mod)>0;
imgen_nueva=imagen.*mask;
%Representacion de todas las mascaras
figure;
Graficas=tiledlayout(2,2);
title(Graficas,'Imagen Ajedrez')
nexttile
imshow(imagen), title('Imagen original');
nexttile
imshow(mask_verde_mod), title('Mascara verde')
nexttile
imshow(mask_magenta_mod), title('Mascara magenta')
nexttile
imshow(mask), title('Mascara total')

% Pasar a RGB la mascara en escala de grises para evitar los problemas de dimensionalidad (triplicar el canal)
lambda=cat(3,mask,mask,mask);

%% Seleccion de parametros -> p = 2
% Proporcionamos los parametros para nuestro algoritmo
varin.lambda    = 100*lambda;   % hyperparametro de fidelidad
varin.Nit       = 2000;         % numero de iteraciones del algoritmo
varin.dt        = 1e-2;         % tamaño del paso 
varin.f         = imagen;       % imagen ruidosa
varin.Verbose   = 1;            % Verbose
varin.im_org    = imagen;       % Imagen original para el computo de la PSNR
varin.p         = 2;

% Ejecutamos el algoritmo
figure;
[varout] = pLap(varin);

% Mostramos el resultado
imagen_inpainting = (varout.u.*(1-mask))+imgen_nueva;

figure
Graficas=tiledlayout(1,2);
title(Graficas,'Imagen Ajedrez')
nexttile
imshow(imagen),title('Imagen Original')
nexttile
imshow(imagen_inpainting),title('Imagen inpainting')

print -dpng ./Imagenes/Resultado_Ajedrez.png