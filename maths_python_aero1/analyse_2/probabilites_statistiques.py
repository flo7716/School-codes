# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:31:55 2022

@author: flori
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import array


def Experience():
    x=rnd.randrange(1,7)
    y=rnd.randrange(1,7)
    z=x+y
    return z

def Experience2(n):
    Val=[2,3,4,5,6,7,8,9,10,11,12]
    Eff=[0,0,0,0,0,0,0,0,0,0,0]
    F=[0]*11
    Eff_C=[0]*11
    F_C=[0]*11
    m=0
    s=0
    for i in range(n):
        z=Experience()
        Eff[z-2]+=1
    for k in range(11):
        F[k]=Eff[k]/n
        Eff_C[k]=Eff[k]+Eff_C[k-1]
        F_C[k]=F[k]+F_C[k-1]
        m+=Val[k]*F[k]
        s+=(Val[k]**2)*F[k]
        v=s-m**2
        e=np.sqrt(v)
    for i in F_C:
        if i>=0.5:
            pass
        else:
            break
    H=F_C.index(i)
    Mediane=Val[H]    
    t=Eff.index(max(Eff))
    Mode=Val[t]
    return Val,Eff,Eff_C,F,F_C,m,v,e,t,Mode,Mediane 

Val,Eff,Eff_C,F,F_C,m,v,e,t,Mode,Mediane=Experience2(10000)
print(Val)
print("effectifs = ",Eff)
print("effectifs cumules = ",Eff_C)
print("Fréquence = ",F)
print("Fréquence cumulée = ",F_C)
print("Moyenne = ",m)
print("Variance = ",v)
print("Ecart-type = ",e)
print(t)
print("Mode = ",Mode)
print("Mediane = ",Mediane)




x=np.array([1,7,1])
plt.bar(Val,F)
plt.show()
plt.plot(Val,F_C)
plt.show()
