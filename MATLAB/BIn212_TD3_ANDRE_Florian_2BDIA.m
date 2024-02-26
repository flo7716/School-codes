%Florian ANDRE 2B DIA BIn212
%TD 3
%Question 1 : 1er signal sinus 1
F0=20;
Fe=8000;
Te=1/Fe;
N=2000;
t=[-N/2:((N/2)-1)]/Fe;
sinus1=sin(2*pi*F0*t);

figure('Name','sinus1 en fonction de t');
plot(sinus1);
title('sinus1 en fonction de t');
xlabel('duree t');
ylabel('amplitude du signal');
grid on;

%Question 2 : 2nd signal sinus 3
Fe=8000;
Te=1/Fe;
t=[-N/2:((N/2)-1)]/Fe;
sinus3=(1/3)*sin(2*pi*3*F0*t);

figure('Name','sinus3 en fonction de t');
plot(sinus3);
title('sinus3 en fonction de t');
xlabel('duree t');
ylabel('amplitude du signal');
grid on;

%somme sinus 1 et sinus 3
sinus4=sinus1+sinus3;

figure('Name','sinus1+sinus3 en fonction de t');
plot(sinus4);
title('sinus1+sinus3 en fonction de t');
xlabel('duree t');
ylabel('amplitude du signal');
grid on;

%Question 3 : 4eme signal sinus 5
Fe=8000;
Te=1/Fe;
t=[-N/2:((N/2)-1)]/Fe;
sinus5=(1/3)*sin(2*pi*5*F0*t);

%somme sinus 1, sinus 3 et sinus 5
sinus6=sinus1+sinus3+sinus5;
figure('Name','Figure 1');
plot(sinus5);
hold on;
plot(sinus6);
title('sinus5 et sinus1+sinus3+sinus5 en fonction de t');
xlabel('duree t');
ylabel('amplitude du signal');
grid on;

%Question 4 : boucle for de 1 à 15

v=1:1:15;
n=find(mod(v,2)~=0); %Elimine les valeurs paires
disp(n);%Renvoie la liste apres elimination des valeurs paires
sinus_i=0;%initialisation
for i=n;
    sinus_i=sinus_i+(1/i)*sin(2*pi*i*F0*t);
end
carre=(pi/4)*sign(sinus1);
figure('Name','Figure 2');
plot(sinus_i);
hold on;
plot(carre);
hold on;
err1=0.05*(pi/4); %Question 5 : affiche les barres d'erreur
plot([0; 2000], [max(carre)-err1; max(carre)-err1]);%barre d'erreur avec -0,05%
hold on;
plot([0; 2000], [max(carre)+err1; max(carre)+err1]);%barre d'erreur avec +0,05%
title('sinus_i et carre en fonction de t');
xlabel('duree t');
ylabel('amplitude du signal');
grid on;

%Question 6 : Variation d'erreur quadratique entre le signal carré et les signaux avec
%nombre variable d'harmoniques

%Boucle for pour l'ajout d'harmoniques au signal sinus_i
% Paramètres
F0 = 1; % Fréquence fondamentale
t = linspace(0, 1, 2000); % Vecteur de temps

% Boucle pour le nombre d'harmoniques
max_harmonics = 100;
erreur_quadratique = zeros(1, max_harmonics);

for num_harmonics = 1:max_harmonics
    % Calcul du signal avec un nombre variable d'harmoniques
    sinus_i = 0;
    for i = 1:2:num_harmonics*2
        sinus_i = sinus_i + (1/i)*sin(2*pi*i*F0*t);
    end
    
    % Calcul du signal carré
    carre = (pi/4)*sign(sinus_i);
    
    % Calcul de l'erreur quadratique
    erreur_quadratique(num_harmonics) = sum((carre - sinus_i).^2);
end

% Affichage de la variation de l'erreur quadratique
figure('Name','Variation de l''erreur quadratique');
semilogy(1:max_harmonics, erreur_quadratique, 'o-');
title('Variation de l''erreur quadratique en fonction du nombre d''harmoniques');
xlabel('Nombre d''harmoniques');
ylabel('Erreur quadratique');
grid on;


