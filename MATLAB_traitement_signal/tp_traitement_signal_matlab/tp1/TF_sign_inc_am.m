
clear all; 
close all; 
clc

load("signal_inconnu.mat");

xk = xk(1:50);

Te =  1/Fs ;
N = length(xk);
t = 0 : Te : (N-1)*Te;
f = 0 : (Fs/(N-1)) : Fs;
M = 10;
N_zeros = M * N;
xk1 = [xk, zeros(1, N_zeros)];

N = length(xk1);
t = 0 : Te : (N-1)*Te;
f = 0 : (Fs/(N-1)) : Fs;

Xn1=fft(xk1);

subplot(2,1,1);
plot(f, abs(Xn1));

xlabel('Fréquence (Hz)');
ylabel('|Xn1|');
title('Module de Xn1');

subplot(2,1,2);
plot(t, xk1);
xlabel('Temps (s)');
ylabel('Amplitude');
title('Signal xk1');
