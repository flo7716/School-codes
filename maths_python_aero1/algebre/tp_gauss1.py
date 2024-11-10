# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:42:07 2023

@author: flori
"""

import numpy as np
import time
import matplotlib.pyplot as plt

def ReductionGauss(A):
    n,m=np.shape(A)
    A=np.copy(A)
    for i in range(n-1):
        if A[i,i]==0:
            print('le pivot est nul')
            return A
        for k in range(i+1,n):
            g=A[k,i]/A[i,i]
            A[k,:]=A[k,:]-g*A[i,:]
    return A 


def Resolutionsystrisup(T,B):
    n,m=np.shape(T)
    X=np.zeros(n)
    X[n-1]=B[n-1]/T[n-1,n-1]
    for j in range (n-2,-1,-1):
        somme=0
        for k in range(j+1,n):
            somme+=T[j,k]*X[k]
        
        X[j]=(1/T[j,j])*(B[j]-somme)
    return X 

def Gauss(A,B):
    n,m=np.shape(A)
    Aaug=np.column_stack([A,B])
    Taug=ReductionGauss(Aaug)
    T=Taug[:,0:n]
    Bmod=Taug[:,n]
    X=Resolutionsystrisup(T,Bmod)
    return X


A=np.random.rand(100,100)
B=np.random.rand(100)
X=Gauss(A,B)
err=np.linalg.norm(A@X-B)
print(err)

debut=time.perf_counter()
X=Gauss(A,B)
err=np.linalg.norm(A@X-B)
duree=time.perf_counter()-debut
print(X)
print(duree,err)


Err=[]
temps=[]
N=[]
L1=[]
L2=[]
L3=[]
listen=list(range(5,50,5))+list(range(50,200,30))+list(range(200,500,25))
for n in listen:
    debut=time.perf_counter()
    N.append(n)
    A=np.random.rand(n,n)
    B=np.random.rand(n)
    X=Gauss(A,B)
    err=np.linalg.norm(A@X-B)
    Err.append(err)
    duree=time.perf_counter()-debut
    temps.append(duree)
    L1.append(n)
    L3.append(duree)
plt.plot(N,Err,label="Erreur")
plt.legend()
plt.show()

plt.plot(N,temps,label="duree")
plt.legend()
plt.show()

    