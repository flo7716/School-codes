#include <iostream>
//required for memory allocation and deallocation
#include <stdlib.h>
#include <string.h>

using namespace std;

void echange(int *a,int *b){
    int z;
    cout<<"\n-------------------------";
    z=*a;
    *a=*b;
    *b=z;
    cout<<"\n-------------------------";
    cout<<"\nApres echange, x="<<*a<<" et y="<<*b;
    cout<<"\n-------------------------";
};


void min_max(int a,int b,int*maxi,int*mini){
    if(a<b)
    {
        *maxi=b;
        *mini=a;
    }
    else
    {
        *maxi=a;
        *mini=b;
    }
};


void saisir_n(int*n){
    do
    {
        cout<<"\nDonnez n : ";
        cin>>*n;
    }while(*n<=0);
};