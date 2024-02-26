%Florian ANDRE 2B DIA BIn212
%TD 2 fonction Ex 5
function [A,r]=MatR(T,m,n)%Avec T entre 0 et 10, m lignes et n colonnes
    if nargin <2 || nargin > 3
        error('Nombre incorrect d''arguments d''entree');
    end

    if nargin == 2
        n=m;%Si le nombre de colonnes n'est pas spécifié, il est égal au nombre de lignes (matrice carrée)
    end
    A=round(randi(T,m,n));

    if nargout == 2
        r=rank(A); %calcule le rang de A si 2 arguments de sortie sont demandé
    end
end