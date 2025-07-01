clear all ; close all ; clc ; % remises à zéro de précaution
% Génération d’echelon unité
% Génération de la base de temps :
t=-10 :1 :10 ;
size(t)
% Génération de l’impulsion
u=[zeros(1,10),ones(1,11)] ;
u2=3*u;
u3=[zeros(-1,8),ones(-1,9)];
size(u) % On vérifie que t et u ont des dimensions compatibles
% On trace le signal
figure(1)
subplot(3,1,1);
stem(t,u) ;
title("Echelon unité") ;
xlabel("Temps (s)") ;
ylabel("Amplitude") ;
grid on ;

subplot(3,1,2);
stem(t,u2) ;
title("Echelon unité") ;
xlabel("Temps (s)") ;
ylabel("Amplitude") ;
grid on ;

subplot(3,1,3);
stem(t,u3) ;
title("Echelon unité") ;
xlabel("Temps (s)") ;
ylabel("Amplitude") ;
grid on ;