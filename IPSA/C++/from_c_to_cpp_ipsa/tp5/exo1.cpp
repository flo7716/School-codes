#include <iostream>

using namespace std;

int main(){
    int a,m,j,a_bissextile,date_correcte ;

     cout<<"Saisissez une annee : ";
    cin>>a;
    if((a%4==0)&&(a%100!=0)||(a%400==0))
        {cout<<a<<" est une annee bissextile";
        a_bissextile=1;
        }
    else
        {cout<<a<<" n'est pas une annee bissextile";
        a_bissextile=0;
        }

    cout<<"\nSaisissez un mois : ";
    cin>>m;
    if(m<1||m>12)
        cout<<m<<" est un numero de mois incorrect : ";
    else
        cout<<m<<" est un numero de mois correct : ";

    cout<<"\nSaisissez un jour : ";
    cin>>j;
    if (m==2)
        {if (a_bissextile==1)
            if(j<1||j>29)
                date_correcte=0;
            else
                date_correcte=1;

        else
            if(j<1||j>28)
                date_correcte=0;
            else
                date_correcte=1;
        }
    if(m==1||m==3||m==5||m==7||m==8||m==10||m==12)
        {if(j<1||j>31)
                date_correcte=0;
        else
                date_correcte=1;
        }
    else
        if(j<1||j>30)
                date_correcte=0;
        else
                date_correcte=1;
    if (date_correcte==1)
        ///Affichage de la date correcte ou incorrecte
        cout<<"\nDate correcte : "<<j<<"/"<<m<<"/"<<a;
    else
        cout<<"\nDate incorrecte : "<<j<<"/"<<m<<"/"<<a;
    
}