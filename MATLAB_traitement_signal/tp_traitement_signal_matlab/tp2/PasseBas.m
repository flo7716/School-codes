%Hector Lamalle / Florian André B2 DIA
% TP 2

clear all;
close all;
clc
% Paramètres du filtre
Fs=8000;
Wp = 2100/(Fs/2); % Fréquence de bande passante (normalisée par Fs/2)
Ws = 2200/(Fs/2); % Fréquence de bande coupée (normalisée par Fs/2)
Rp = 1; % Atténuation maximale (en dB) dans la bande passante
Rs = 50; % Atténuation minimale (en dB) dans la bande coupée

% Estimation de l'ordre minimal nécessaire et de la fréquence de coupure à -3dB
[N, Wn] = buttord(Wp, Ws, Rp, Rs);

disp(['Ordre du filtre : ', num2str(N)]);
disp(['Fréquence de coupure à -3dB : ', num2str(Wn)]);

% Calcul des coefficients du filtre
[B, A] = butter(N, Wn);

disp(B);
disp(A);

[Rf,fr]=freqz(B,A,1024,Fs);
plot(fr,abs(Rf));