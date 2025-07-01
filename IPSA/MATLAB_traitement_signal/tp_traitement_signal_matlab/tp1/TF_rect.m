clear all; 
close all; 
clc

Te=0.05;
Ta=51.2;
N=Ta/Te;
t=0:Te:(N-1)*Te;
fe=1/Te;
f=0:(fe/(N-1)):fe;
f_d=-fe/2:(fe/(N-1)):fe/2;

x1=rectpuls(t-0.5);
X=fft(x1);
Y=fftshift(X);

subplot(3,1,1);
plot(t,x1);
title("Signal rectangulaire x(t)")

subplot(3,1,2);
plot(f, abs(X));
title("Spectre de la transformée de Fourier de x(t)")

subplot(3,1,3);
plot(f_d,abs(Y));
title("Spectre de la transformée de Fourier décalée de x(t)")