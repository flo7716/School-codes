#include <stdio.h>
#include <stdlib.h>
//Florian ANDRE 2BDIA
//BIn211 TP8
typedef struct element{
    int valeur;
    struct element* suivant;
}element;

typedef element* Liste;

void afficher_liste(Liste L)
{
    if(L==NULL)
    {
        printf(" --> NULL");
        printf("\n");
    }
    else
    {
        printf(" --> %d",L->valeur);
        afficher_liste(L->suivant);
    }
}

Liste ajout_liste_tete(Liste L, int val)
{
    Liste P;
    P=(element*)malloc(sizeof(element));
    P->valeur=val;
    if(L==NULL)
    {
        P->suivant=NULL;
    }
    else
    {
        P->suivant=L;
    }
    return(P);
}


Liste ajout_liste_queue(Liste L, int val)
{
    if(L==NULL)
    {
        Liste P;
        P=(element*)malloc(sizeof(element));
        P->valeur=val;
        P->suivant=L;
        return(P);
    }
    else
        L->suivant=ajout_liste_queue(L->suivant,val);
}


int taille_liste(Liste L)
{

    if(L==NULL)
        return(0);
    else
        return(1+taille_liste(L->suivant));
}

int recherche_liste(Liste L,int val)
{
    if(L==NULL)
        return(0);
    else
    {
        if(L->valeur==val)
            return(1+recherche_liste(L->suivant,val));
        else
            return(0+recherche_liste(L->suivant,val));
    }
}


Liste suppression_debut(Liste L)
{
    if (L == NULL)
    {
        printf("La liste est vide, suppression impossible.\n");
        return NULL;
    }

    Liste temp = L->suivant;
    free(L);
    return temp;
}

Liste suppression_fin(Liste L)
{
    if (L == NULL)
    {
        printf("La liste est vide, suppression impossible.\n");
        return NULL;
    }

    if (L->suivant == NULL)
    {
        free(L);
        return NULL;
    }

    Liste temp = L;
    while (temp->suivant->suivant != NULL)
    {
        temp = temp->suivant;
    }

    free(temp->suivant);
    temp->suivant = NULL;
    return L;
}

Liste suppression_milieu(Liste L, int val)
{
    if (L == NULL)
    {
        printf("La liste est vide, suppression impossible.\n");
        return NULL;
    }

    if (L->valeur == val)
    {
        Liste temp = L->suivant;
        free(L);
        return temp;
    }

    Liste prec = L;
    Liste temp = L->suivant;

    while (temp != NULL && temp->valeur != val)
    {
        prec = temp;
        temp = temp->suivant;
    }

    if (temp == NULL)
    {
        printf("La valeur %d n'a pas été trouvée dans la liste.\n", val);
        return L;
    }

    prec->suivant = temp->suivant;
    free(temp);
    return L;
}

main()
{
    Liste L,P;
    int taille,val,R;
    L=NULL;
    P=(element*)malloc(sizeof(element));
    P->valeur=0;
    P->suivant=NULL;
    L=P;
    afficher_liste(L);

    L=ajout_liste_tete(L,-3);
    afficher_liste(L);
    L=ajout_liste_tete(L,1);
    afficher_liste(L);
    L=ajout_liste_tete(L,2);
    afficher_liste(L);
    L=ajout_liste_tete(L,3);
    afficher_liste(L);
    L=ajout_liste_queue(L,-1);
    afficher_liste(L);
    L=ajout_liste_queue(L,-2);
    afficher_liste(L);
    L=ajout_liste_queue(L,-3);
    afficher_liste(L);

    taille=taille_liste(L);
    printf("\n");
    printf("Taille : %d",taille);
    printf("\n");

    printf("Donnez la valeur a rechercher : ");
    scanf("%d",&val);
    R=recherche_liste(L,val);
    printf("\nNombre d'occurences de la valeur recherchee : %d",R);


    // Suppression au début
    printf("\nSuppression au debut:\n");
    L = suppression_debut(L);
    afficher_liste(L);

    // Suppression à la fin
    printf("\nSuppression a la fin:\n");
    L = suppression_fin(L);
    afficher_liste(L);

    // Suppression au milieu (par exemple, suppression de la valeur 2)
    printf("\nSuppression au milieu (valeur 2):\n");
    int val_suppression = 2;
    L = suppression_milieu(L, val_suppression);
    afficher_liste(L);

}

