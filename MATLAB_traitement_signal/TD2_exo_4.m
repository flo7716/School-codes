clear all ; close all ; clc ; % remises à zéro de précaution
% Génération d’une impulsion de Dirac
% Génération de la base de temps :
t=-10 :1 :20 ;
size(t)
% Génération de l’impulsion
u=[zeros(1,10) 1 zeros(1,20)] ;
u2=3*u ;
u3=2*[zeros(1,12) 1 zeros(1,18)] ;
size(u) % On vérifie que t et u ont des dimensions compatibles
% On trace le signal
figure(1)
subplot(3,1,1);
stem(t,u) ;
title("Impulsion de Dirac") ;
xlabel("Temps (s)") ;
ylabel("Amplitude") ;
grid on ;

subplot(3,1,2);
stem(t,u2);
title("Impulsion de Dirac") ;
xlabel("Temps (s)") ;
ylabel("Amplitude") ;
grid on ;

subplot(3,1,3);
stem(t,u3);

title("Impulsion de Dirac") ;
xlabel("Temps (s)") ;
ylabel("Amplitude") ;
grid on ;

