%Florian ANDRE 2B DIA BIn212
%TD 1

%EXERCICE 1
disp("Exercice 1");
%Question 1
x=[19 8 10 13 6 15 9 18 16 12 11 17];

%Question 2
N=length(x);
disp(['La longueur du vecteur x est : ',num2str(N)]);

%Question 3
S=sum(x);
disp(['La somme des elements du vecteur x est : ',num2str(S)]);

%Question 4
Moy=mean(x);
ET=std(x);
disp(['La moyenne des elements du vecteur x est : ',num2str(Moy)]);
disp(['L ecart type des elements du vecteur x est : ' ,num2str(ET)]);

%Question 5
dx=diff(x);
disp(['Le vecteur dx vaut : ',mat2str(dx)]);

%Question 6
t = linspace(-25,25,51);
disp(["Le vecteur t est egal a : ",mat2str(t)]);

%Question 7 
y=t.^2;
disp(["Le vecteur y est egal a : ",mat2str(y)]);

%Question 8
z=(flip(t)).^3;
disp(["z^3 = ", mat2str(z)]);

%Question 9
somme_positifs_z=sum(z(z>0));
disp(["La somme des elements positifs de z est egale a : ",num2str(somme_positifs_z)]);


%EXERCICE 2
disp("Exercice 2");
%Question 1
t1=(1:0.5:10)';
disp(['Vecteur t1 : ',mat2str(t1)]);

%Question 2
A=[t,t.^2, t.^3, t.^4];
disp(['Matrice A : ',mat2str(A)]);

%Question 3
colonne_conditionnelle = t>5;
A=[A,colonne_conditionnelle];
disp(['Matrice A apres colonne conditionnelle : ',mat2str(A)]);

%Question 4
colonne_entier=(t==round(t))*5;
A=[A,colonne_entier];
disp(['Matrice A apres colonne_entier : ',mat2str(A)]);



%EXERCICE 3
disp("Exercice 3");
%Structures
u1=[1 2 3];
u2=[-5 2 1];
u3=[-1 -3 7];
A=[2 3 4;7 6 5;2 8 7];
sum_vect=u1+3.*u2-u1/5
prod_scal=u1*u2'
prod_A=A.*u1
disp(['Le produit u1+3*u2-u1/5 est egal a : ',num2str(sum_vect)]);
disp(['Le produit scalaire entre les vecteurs u1 et u2 est egal a : ',num2str(prod_scal)]);
disp(["le produit entre la matrice A et le vecteur u1 est egal a : ",mat2str(prod_A)]);

%Commandes
%Question a
normeu1=norm(u1,2);
normeu2=norm(u2,1);
normeu3=norm(u3,Inf);
disp(['norme u1 : ',num2str(normeu1)]);
disp(['norme u2 : ',num2str(normeu2)]);
disp(['norme u3 : ',num2str(normeu3)]);

%Question b
dimension_A=size(A);
disp(["dimension de A : ",num2str(dimension_A)]);

%Question c
determinant_A=det(A);
disp(["Determinant de A : ",num2str(determinant_A)]);
inverse_A=inv(A);
disp(["inverse de A : ",mat2str(inverse_A)]);

%Resolution systemes lineaires
% factorisation LU de A
[P, L, U] = lu(A);

% Résolvons le système A*x = u1 en utilisant la factorisation LU
y = L \ (P .* u1);
x = U \ y;

%Matrice inverse
% Résolvons le système A*x = u1 en utilisant l'inverse de A
%x = A \ u1;
disp(["Matrice x resolvant le systeme : ",mat2str(x)]);


