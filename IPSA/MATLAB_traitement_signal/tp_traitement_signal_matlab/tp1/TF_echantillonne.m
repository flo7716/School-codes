clear all; 
close all; 
clc

fe = 300;
Te = 1/fe;
F=40;

N=100;

t=0:Te:(N-1)*Te;
f=0:(fe/(N-1)):fe;
f_d=-fe/2:(fe/(N-1)):fe/2;

x0=3;
x1=x0 * cos(2 * pi* F*t);
X=fft(x1);
Y=fftshift(X);

xr = ifft(X);

subplot(4,1,1);
plot(t,x1);
title("Signal rectangulaire x(t)")

subplot(4,1,2);
plot(t,xr);
title("inverse de la TF")

subplot(4,1,3);
plot(f, abs(X));
title("Spectre de la transformée de Fourier de x(t)")

subplot(4,1,4);
plot(f_d,abs(Y));
title("Spectre de la transformée de Fourier décalée de x(t)")