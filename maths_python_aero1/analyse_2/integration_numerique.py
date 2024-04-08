# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:09:42 2023

@author: flori
"""


from numpy import pi
from math import log
from math import exp
from math import cos
from math import sin
import matplotlib.pyplot as plt 
from numpy import linspace
import numpy as np

def f(x):
    return 1/x**2


def RD(f,a,b,N):
    S=0
    h=(b-a)/N
    for i in range (N):
        S=S+f(a+(i+1)*h)
    S=h*S
    return S

def RG(f,a,b,N):
    h=(b-a)/N
    S=0
    for i in range(N):
        S=S+f(a+i*h)
    S=h*S
    return S

def PM(f,a,b,N):
    h=(b-a)/N
    S=0
    for i in range(N):
        S=S+f(a+(i+1/2)*h)
    S=h*S
    return S

def TR(f,a,b,N):
    h=(b-a)/N
    S=(f(a)+f(b))/2
    for i in range(1,N):
        S=S+f(a+i*h)
    S=h*S
    return S

N10=TR(f,2,4,10)
N50=TR(f,2,4,50)
N1000=TR(f,2,4,1000)

print(N10,N50,N1000)
  

Err1=[]
Err2=[]
Err3=[]
Err4=[]
LN=[]
for N in range(1,100):
    LN.append(N)
    S1=PM(f,2,4,N)
    S2=RG(f,2,4,N)
    S3=RD(f,2,4,N)
    S4=TR(f,2,4,N)
    Err1.append(abs(S1-1/4))
    Err2.append(abs(S2-1/4))
    Err3.append(abs(S3-1/4))
    Err4.append(abs(S4-1/4))
plt.semilogy(LN,Err1,label="PM")
plt.semilogy(LN,Err2,label="RD")
plt.semilogy(LN,Err3,label="RG")
plt.semilogy(LN,Err4,label="TR")
plt.legend()
plt.show()



# S_RD=RD(f,2,4,100)
# S_RG=RG(f,2,4,100)
# S_PM=PM(f,2,4,100)
# S_TR=TR(f,2,4,100)

# print(S_RD,S_RG,S_PM,S_TR)


def f1(x):
    return log(x+1)/x**2

def f2(x):
    return exp(cos(x))

def f3(x):
    return sin(x**2)

def f4(x): 
    return x**2

def g(x):
    def f(t):
        return  exp(-t**2)
    return PM(f,-x,2*x,1000)




I1=PM(g,1,3,100)
I2=PM(f2,0,pi,100)
I3=PM(f3,-1,1,100)
I4=PM(f4,0,3,100)


print(I1,I2,I3)
print("solution approchée pour f3 de l'exo 3 est:",I1)



x=linspace(-3,3,100)
y=f4(x)
plt.plot(x,y)
plt.show() 

n=np.size(x)
y=np.zeros(n)
for i in range(n):
   y[i]=g(x[i])
plt.plot(x,y)
plt.show() 



