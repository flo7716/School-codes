function M=GenererM(x,n)
    %Prend en arguments d'entree un vecteur réel x et n un entier positif
    m = length(x);
    if m<n
        error('Erreur : m doit etre superieur ou egal a n+1');
    end
    
    %Preallocation de la matrice avec 1
    M=ones(m,n+1);
    
    %Remplissage colonne par colonne avec 1 seule boucle for
    for j=2:n+1
        M(:,j)=cos(j*x);
    end
end
