%Florian ANDRE 2B DIA
%TD 4 BIn212
%Partie I:
%Question 1 : 
x=linspace(-10,10,100);
%La syntaxe correcte est la réponse C (opérateurs .* pour multiplier chaque
%élément de la matrice et .^ pour la puissance)
y=sqrt(x+6).*sin(x).^2;
disp(y);
%%
%Question 2 : 

N=1000; F0 =50; Fe = 5000;
t = [(-N/2)/Fe : ((N/2)-1)/Fe];
SINUS = 4* sin(2* pi* Fe *t);
disp(["SINUS = ",mat2str(SINUS)]);

%La syntaxe correcte est la réponse C

%%
%Question 3 : 
x=[1,1];
y=[1,1];
plot(x,y,'r*');
%La bonne syntaxe est la syntaxe D

%%
%Question 4 : 
x=linspace(-5,5,1001);
y1=cos(2*pi*x);
y2=sin(2*pi*x);
figure

subplot(1,1,1);
plot(x,y1);
figure
subplot(2,1,2);
plot(x,y2);
%La bonne syntaxe est la réponse C
%%
%Question 5 : 
subplot(3,1,1);
plot(x,y1);
figure
subplot(3,1,2);
plot(x,y2);
subplot(3,1,3);
plot3(y1,y2,x);
%La bonne syntaxe est la réponse C (elle affiche les 2 dernières courbes sur 1
%figure)
%%
%Question 6 : 
a=linspace(-2,2,4);
n=1;
for i=1:n-1
    a(i)=b(i+1)-b(i);
end
disp(a);

for i=1:n-1
    a(i)=b(2:n)-b(1:n-1);
end
disp(a);

%La réponse correcte est la réponse A
%%
%Question 7
%On souhaite manipuler les éléments du vecteur v. Notre boucle for doit
%aller du premier au dernier élément du vecteur (càd un nombre)
%La syntaxe correcte est la syntaxe B

%%
%Question 8
disp(SommeDifference(2,3));
%Question A : Faux car la fonction ne renvoie que 5
%Question B : Faux. Aucune erreur car le nombre d'arguments est correct
%Question C : Faux car la fonction ne renvoie que 5
%Question D : Faux car la fonction renvoie 5 7

%%
%Partie II
%Exercice 1
M1=GenererM([6 0 0],3);
M2=GenererM([2 2 0],3);
disp(M1);
disp(M2);
%%
%Exercice 2
thetha=linspace(0,2*pi,100);
x=cos(thetha);
y=sin(thetha);
for a=1:10
    %tracé du cercle
    plot(x*a+a,y*a,'b','LineWidth',1);
    hold on
    plot(21-(x*a+a),y*a, 'r', 'LineWidth', 1);
    
end

axis equal;
xlabel('x');
ylabel('y');
legend('Cercles bleus','Cercles rouges');
grid on;

%%
%Exercice 3
%1 Couture
th=linspace(0,2*pi,1000);
a=3;
b=1;
c=2*sqrt(a*b);

x = a*cos(t) + b*cos(3*t);
y = a*sin(t) - b*sin(3*t);
z = c*sin(2*t);
figure
plot3(x,y,z,'LineWidth',2);



%2 Variation des paramètres
parametres_courbes=[0,1,2*sqrt(0);0.5,1,2*sqrt(0.5);1,1,2*sqrt(1)];

nb_points=1000;
t=linspace(0,2*pi,nb_points);

figure %initialise la figure

%Boucle pour faire les 3 courbes
for i=1:3
    a=parametres_courbes(i,1);
    b=parametres_courbes(i,2);
    c=parametres_courbes(i,3);

    x = a*cos(t) + b*cos(3*t);
    y = a*sin(t) - b*sin(3*t);
    z = c*sin(2*t);
    % Tracer la courbe avec une couleur différente pour chaque courbe
    subplot(1, 3, i);
    plot3(x, y, z, 'LineWidth', 1.5);
    grid on;
    title(['Courbe \Gamma', num2str(i)]);
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
    axis equal;
end
