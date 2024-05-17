#include <stdio.h>
#include <stdlib.h>
//Florian ANDRE 2BDIA
//BIn211 TP8
typedef struct element
{
    int valeur;
    struct element *suivant;
} element;

typedef element *Liste;

void afficher_liste(Liste L)
{
    if (L == NULL)
    {
        printf(" --> NULL");
        printf("\n");
    }
    else
    {
        printf(" --> %d", L->valeur);
        afficher_liste(L->suivant);
    }
}

Liste ajout_liste_tete(Liste L, int val)
{
    Liste P;
    P = (element *)malloc(sizeof(element));
    P->valeur = val;
    if (L == NULL)
    {
        P->suivant = NULL;
    }
    else
    {
        P->suivant = L;
    }
    return (P);
}

Liste ajout_liste_queue(Liste L, int val)
{
    if (L == NULL)
    {
        Liste P;
        P = (element *)malloc(sizeof(element));
        P->valeur = val;
        P->suivant = L;
        return (P);
    }
    else
        L->suivant = ajout_liste_queue(L->suivant, val);
    return L;
}

int taille_liste(Liste L)
{
    if (L == NULL)
        return (0);
    else
        return (1 + taille_liste(L->suivant));
}

int recherche_liste(Liste L, int val)
{
    if (L == NULL)
        return (0);
    else
    {
        if (L->valeur == val)
            return (1 + recherche_liste(L->suivant, val));
        else
            return (0 + recherche_liste(L->suivant, val));
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

int main()
{
    Liste L, P;
    int taille, val, R, choix;
    L = NULL;
    P = (element *)malloc(sizeof(element));
    P->valeur = 0;
    P->suivant = NULL;
    L = P;
    afficher_liste(L);

    do
    {
        printf("\n\nMenu :\n");
        printf("1- Ajouter en tete de liste chainee\n");
        printf("2- Ajouter en queue de liste chainee\n");
        printf("3- Afficher une liste chainee\n");
        printf("4- Taille d'une liste chainee\n");
        printf("5- Chercher un element specifique dans une liste chainee\n");
        printf("6- Supprimer en tete de liste chainee\n");
        printf("7- Supprimer en queue de liste chainee\n");
        printf("8- Supprimer un element specifique de la liste chainee\n");
        printf("9- Sortir\n");

        printf("\nChoix : ");
        scanf("%d", &choix);

        if (choix == 1)
        {
            printf("Donnez la valeur a ajouter en tete : ");
            scanf("%d", &val);
            L = ajout_liste_tete(L, val);
        }
        else if (choix == 2)
        {
            printf("Donnez la valeur a ajouter en queue : ");
            scanf("%d", &val);
            L = ajout_liste_queue(L, val);
        }
        else if (choix == 3)
        {
            afficher_liste(L);
        }
        else if (choix == 4)
        {
            taille = taille_liste(L);
            printf("Taille : %d\n", taille);
        }
        else if (choix == 5)
        {
            printf("Donnez la valeur a rechercher : ");
            scanf("%d", &val);
            R = recherche_liste(L, val);
            printf("Nombre d'occurences de la valeur recherchee : %d\n", R);
        }
        else if (choix == 6)
        {
            L = suppression_debut(L);
        }
        else if (choix == 7)
        {
            L = suppression_fin(L);
        }
        else if (choix == 8)
        {
            printf("Donnez la valeur a supprimer : ");
            scanf("%d", &val);
            L = suppression_milieu(L, val);
        }
        else if (choix == 9)
        {
            printf("Au revoir !\n");
        }
        else
        {
            printf("Choix invalide. Veuillez choisir un nombre entre 1 et 9.\n");
        }
    } while (choix != 9);

    // Libérer la mémoire
    while (L != NULL)
    {
        Liste temp = L->suivant;
        free(L);
        L = temp;
    }

    return 0;
}
