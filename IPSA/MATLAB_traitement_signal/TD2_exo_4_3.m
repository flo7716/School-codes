% TD 2 EXO 4 Q3
t=[0,10*pi];
% Définition du pas de temps
Te = 0.1;

% Définition de la base de temps
t = 0:Te:10*pi;

f1=0.1;
x1=sin(2*pi*f1*t);
figure(1);
plot(t,x1);
title('sinus');
xlabel('t');
ylabel('amplitude');
grid on;