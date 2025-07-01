%Florian ANDRE 2B DIA BIn212
%TD 2

%EXERCICE 1 : conversion qté énergie avec Switch-Case
%Sert a demander la valeur d'energie, son unite et la nouvelle unite
disp("Exercice 1");
V_in = input("Qté d'énergie à convertir : ");
Ein_unit = input('Entrer l''unité (J,ft-lb,cal ou eV) : ','s');
Eout_unit = input('Entrer l''unité désirée(J,ft-lb,cal ou eV) : ','s');

%Utilise une structure switch pour choisir entre les unites d'entree
switch Ein_unit
    case 'J'
        E_Joule = V_in;
    case 'ft-lb'
        E_Joule = V_in/0.738;
    case 'cal'
        E_Joule = V_in/0.239;
    case 'eV'
        E_Joule = V_in/(6.24*10^28);
    otherwise
        disp('L''unité d''entrée n''est pas correcte!');
        return
end

%Utilise une autre structure switch pour choisir entre les unites de sortie
switch Eout_unit
    case 'J'
        E_new=E_Joule;
    case 'ft-lb'
        E_new=E_Joule*0.738;
    case 'cal'
        E_new=E_Joule*0.239;
    case 'eV'
        E_new=E_Joule*6.24e18;
    otherwise
        disp('L''unité de sortie n''est pas correcte!');
        return
end

fprintf('%g %s = %g %s\n', V_in, Ein_unit, E_new, Eout_unit)

%On obtient les résultats suivants : 325 J = 239.85 ft-lb , 432 cal =
%1807.53 J, et 6.8 eV = 2.60449e-29 cal


%Exercice 2 : Série de Taylor
disp("Exercice 2 : Serie de Taylor : ");
x=input('x = ');
n=20; %Nombre maximal de passages
i=0; %Initialisation nombre de passages
f=1;
while i<=n
    last_term=(x.^i)/factorial(i);
    if (x.^i)/factorial(i)<0.0001
        msgbox('Last term is smaller than 0.0001 and hence stopped')
        break
    elseif i==n && last_term>0.0001
        msgbox('More steps needed')
        break
    end
    f=f+last_term;
    i=i+1;
end
y=f-1;

%Le programme renvoie les résultats suivants : pour e^3 y = 20.0855, pour
%e^-5 y=1 et pour e^20 = "More steps needed" car l'approximation n'est pas
%précise

%Exercice 3 : Nombre d'or
disp('Exercice 3 : nombre d''or :');
n=100;%Taille du vecteur A
A=ones(1,n);
A(1)=1;
A(2)=1;

%Calcul du vecteur A
for i = 3:n
    A(i)=A(i-1)+A(i-2);
end

%Initialisation du vecteur r
r=zeros(1,n);

%Calcul de r
for i = 2:n
    r(i)=A(i)/A(i-1);
end

%Plot r en fonction de A(i) et A(i-1)
figure('Name','r en fonction de A(i) et A(i-1)');
plot(r);
title('Nombre d''or');
xlabel('Indice i');
ylabel('Valeur de r');
grid on;


%Plot r selon echelle logarithmique
%sur x
figure('Name','Echelle logarithmique selon x');
plot(abs(r-r(n)));
title('Nombre d''or echelle log selon x');
xlabel('Indice i');
ylabel('Valeur de r');
grid on
xscale log

%sur y
figure('Name','Echelle logarithmique selon y');
plot(abs(r-r(n)));
title('Nombre d''or echelle log selon y');
xlabel('Indice i');
ylabel('Valeur de r');
grid on
yscale log

%sur x et y
figure('Name','Echelle logarithmique selon x et y');
plot(abs(r-r(n)));
title('Nombre d''or echelle log selon x et y');
xlabel('Indice i');
ylabel('Valeur de r');
grid on
yscale log


%Alternative à la fonction plot et xscale yscale
%Plot r selon echelle logarithmique
%sur x
figure('Name','Echelle logarithmique selon x');
y=abs(r-r(n));
title('Nombre d''or echelle log selon x');
xlabel('Indice i');
ylabel('Valeur de r');
loglog(y);
grid on



%Exercice 4
disp('Exercice 4 : Jeu de hasard');
X=round(rand()*10);
nb_essais=0;
nb_essais_max=3;

while nb_essais<nb_essais_max
    nb_utilisateur=input('Saisissez un nombre entre 0 et 10 : ');
    if nb_utilisateur==X
        disp("Winner !");
        break %car le joueur a gagné
    elseif nb_utilisateur<X
        disp('C''est petit');
    else
        disp('C''est grand');
    end
    nb_essais=nb_essais+1;
end

if nb_essais==nb_essais_max % cas où le joueur ne trouve pas le bon nombre apres 3 iterations
    disp(['Loser ! Le nombre correct etait : ',num2str(X)]);
end

%Exercice 5
disp("Exercice 5 : Rang d'une matrice aléatoire");
disp("Matrice 4*5 : ");
[A,r]=MatR(10,4,5);
disp(["A = ",mat2str(A)]);
disp(["Le rang de la matrice est egal a : ",num2str(r)]);

disp("Matrice carrée : ");
A=MatR(10,3);
disp(["A = ",mat2str(A)]);
disp(["Le rang de la matrice est egal a : ",num2str(r)]);
