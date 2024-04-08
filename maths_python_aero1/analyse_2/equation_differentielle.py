# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:41:27 2023

@author: flori
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return y

# def Euler(f,a,b,y0,N):
#     h=(b-a)/N
#     x=0
#     y=y0
#     X=[x]
#     Y=[y]
#     for i in range(N):
#         y=y+h*f(x,y)
#         x=x+h
#         X.append(x)
#         Y.append(y)
#     return(X,Y) 

# X,Y=Euler(f,0,1,1,10)
# print(Y)
# S=[np.exp(x) for x in X]

# plt.plot(X,Y,label='Solution approchée')
# plt.plot(X,S,label='solution exacte')
# plt.legend()
# plt.show()


def Euler2(f,a,b,y0,z0,N):
    h=(b-a)/N
    x=a
    y=y0
    z=z0
    X=[x]
    Y=[y]
    Z=[z]
    for i in range(N):
        buffer=f(x,y,z)
        y=y+h*z
        x=x+h
        z=z+h*buffer
        X.append(x)
        Y.append(y)
        Z.append(z)
    return(X,Y,Z)

def f1(x,y,z):
    return y**2+1


X,Y,Z=Euler2(f1,0,5,1,1,10)
print(X)
print(Y)
S=[np.sin(x) for x in X]

plt.plot(X,Y,label='Solution approchée')
plt.plot(X,S,label='solution exacte')
plt.legend()
plt.show()


