#include <iostream>
#include "bibliopointeur.h"

//----------------------------------------------
//Florian ANDRE
//2B DIA
//BIn211 TP6
//----------------------------------------------

int main()
{
    int x,y,mini,maxi,n;
    cout<<"Saisissez x ";
    cin>>x;
    cout<<"Saisissez y ";
    cin>>y;
    echange(&x,&y);
    min_max(x,y,&maxi,&mini);
    cout<<"\nLe maximum est : "<<maxi;
    cout<<"\nLe minimum est : "<<mini;
    saisir_n(&n);
}