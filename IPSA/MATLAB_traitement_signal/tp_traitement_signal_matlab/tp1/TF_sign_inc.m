clear all; 
close all; 
clc

load("signal_inconnu.mat");
xk = xk(1:50);


Te =  1/Fs ;
N = length(xk);
t = 0 : Te : (N-1)*Te;
f = 0 : (Fs/(N-1)) : Fs;

Xn=fft(xk);

subplot(2,1,1)
plot(f,abs(Xn));

subplot(2,1,2)
plot(t , xk)


