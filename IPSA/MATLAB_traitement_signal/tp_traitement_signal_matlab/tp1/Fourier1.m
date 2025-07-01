clear all; 
close all; 
clc

%Génération du signal x1(t)
NbP=1000;
NbHarm=50;
Fp=1;
Tp=1;
Tmax=2*Tp;

delta_t = Tmax/NbP;


t=0 : delta_t : Tmax-delta_t;

x1=square(2*pi*Fp*t,50)+1;


%Calcul de l'harmonique k et reconstruction du signal

SignalR=mean(x1);
Spectre=zeros(NbHarm,1);
for k=1:NbHarm
    Ck=mean(x1.*exp(-2*pi*j*k*Fp*t));
    Ca=abs(Ck); Phik=angle(Ck);
    Spectre(k)=Ca;
    Harmonique=2*Ca*cos(2*pi*k*Fp*t+Phik);
    SignalR=SignalR+Harmonique;
end


%Représentation graphique de x1(t) et de k
subplot(2,1,1)
plot(t, x1)
grid on;
title('signal x_1(t)');

subplot(2,1,2)
plot(t,x1)
hold on
plot(t,SignalR)
grid on;
title('harmonique k et reconstitution du signal')

%Visualisation du spectre de x1
figure(2);
stem(Spectre)
