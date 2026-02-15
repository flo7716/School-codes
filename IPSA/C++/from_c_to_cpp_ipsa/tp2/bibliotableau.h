#include <iostream>
#include <cmath>
#define nmax 50
using namespace std;



//------------------------------
// Fonctions utilitaires tableau
//------------------------------
// Fonction produit
//------------------------------
int produit_tableau( int t[nmax], int n ){  
    int p,i ;
    p =1;
    for(i=0; i<n; i=i+1){
        p = p*t[i];
    return(p);
}

//----------------------------------
// Fonction somme
//----------------------------------
int somme_tableau( int t[nmax], int n ){  
    int s,i ;
    s=0;
    for(i=0; i<n; i=i+1){
        s+=t[i];
    }
    return(s);
}

//----------------------------------
// Fonction moyenne
//----------------------------------

float moyenne( int t[nmax], int n){
    return((float)somme_tableau(t,n)/(float)n);
}

//----------------------------------
// Fonction minimum
//----------------------------------
int minimum_tableau( int t[nmax], int n ){  
    int mini,i ;
    mini = t[0];
    for(i=0; i<n; i++){
        if (t[i]<mini)        {
            mini = t[i];
        }
    }
    return(mini);
}   

//----------------------------------
// Fonction position minimum
//----------------------------------
int pos_minimum_tableau( int t[nmax], int n ){  
    int pos_mini,mini,i ;
    mini = t[0];
    pos_mini = 0;
    for(i=0; i<n; i++){
        if (t[i]<mini)        {
            mini = t[i];
            pos_mini = i;
        }
    }
    return(pos_mini);
}


//----------------------------------
// Fonction maximum
//----------------------------------
int maximum_tableau( int t[nmax], int n ){  
    int m,i ;
    m = t[0];
    for(i=0; i<n; i++){
        if (t[i]>m)        {
            m = t[i];
        }
    }
    return(m);
}
//----------------------------------
// Fonction position maximum
//----------------------------------    
int pos_maximum_tableau( int t[nmax], int n ){  
    int pos_m, m,i ;
    m = t[0];
    pos_m = 0;
    for(i=0; i<n; i++){
        if (t[i]>m)        {
            m = t[i];
            pos_m = i;
        }
    }
    return(pos_m);
}