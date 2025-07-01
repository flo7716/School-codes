# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 09:39:40 2023

@author: flori
"""

from math import sin
from math import cos
from math import sqrt
from math import pi
from math import exp
from math import tan
from math import log

def f(x):
    return 2*x-sin(x)-1

def fder(x):
    return 2-cos(x)

def Newton(f,fder,x0,epsilon,Nitermax):
    x=x0
    Niter=0
    while abs(f(x))>epsilon and Niter<Nitermax:
        x=x-f(x)/fder(x)
        Niter+=1
    return(x,Niter) 

def fexam3(x):
    return x-log(x)-2
def fexam3der(x):
    return 1-1/x
print(Newton(fexam3,fexam3der,1.1,10e-6,1000))

# def fexam4(x):
#     return cos(x)-log(x)
# def fexam4der(x):
#     return -sin(x)-1/x
# print(Newton(fexam4,fexam4der,1,10e-6,1000))

# def fexam5(x):
#     return 3*x**5+10**3*x**3+10**4*x-10**10
# def fexam5der(x):
#     return 15*x**4+30*x**2+10**4
# print(Newton(fexam5,fexam5der,1,10e-6,1000))

# def fexam1(x):
#     return exp(x)-x-3
# def fexam1der(x):
#     return exp(x)-11
# print(Newton(fexam1,fexam1der,1.2,10e-6,1000))

# def fexam2(x):
#     return x**3+sin(x)-8
# def fexam2der(x):
#     return 3*x**2+cos(x)
# print(Newton(fexam2,fexam2der,1.2,10e-6,1000))


# def f1(x):
#     return x**2*exp(x)-8
# def f1der(x):
#     return 2*x*exp(x)+x**2*exp(x)
# print(Newton(f1,f1der,1.2,1e-10,1000))


# def f2(x):
#     return exp(x)+sin(x)-9
# def f2der(x):
#     return exp(x)+cos(x)
# print(Newton(f2,f2der,1.2,1e-10,1000))


# def f3(x):
#     return 3*x+x**3-2
# def f3der(x):
#     return 3+3*x**2
# print(Newton(f3,f3der,1.2,1e-10,1000))

# def f4(x):
#     return 3*x+x**3-9
# def f4der(x):
#     return 3+3*x**2
# print(Newton(f4,f4der,1.2,1e-10,1000))

# def f5(x):
#     return x**4+2*x-11
# def f5der(x):
#     return 4*x**3+2
# print(Newton(f5,f5der,1.2,1e-10,1000))


# def f6(x):
#     return x-2*cos(x)+3
# def f6der(x):
#     return 1+2*sin(x)
# print(Newton(f6,f6der,1.2,1e-10,1000))


# def f7(x):
#     return exp(x)-2*x-12
# def f7der(x):
#     return exp(x)-2
# print(Newton(f7,f7der,1.2,1e-10,1000))


# def f8(x):
#     return 2*tan(x)-x-1
# def f8der(x):
#     return 2*tan(x)**2+1
# print(Newton(f8,f8der,1.2,1e-10,1000))


# def f9(x):
#     return exp(x)-x**4-3
# def f9der(x):
#     return exp(x)-4*x**3
# print(Newton(f9,f9der,1.2,1e-10,1000))

# def f10(x):
#     return x**4-2*x**2+4*x-17
# def f10der(x):
#     return 4*x**3-4*x+4
# print(Newton(f10,f10der,1.2,1e-10,1000))

# def f11(x):
#     return exp(x)*log(x**4+4)-5
# def f11der(x):
#     return (4*log(x**4+4)*exp(x)+4*x**3*exp(x)+x**4*log(x**4+4)*exp(x))/(x**4+4)
# print(Newton(f11,f11der,1.2,1e-10,1000))


# def fexamblanc1(x):
#     return x**4-2*x**2+4*x-17
# def fderexamblanc1(x):
#     return 4*x**3-4*x+4
# print(Newton(fexamblanc1,fderexamblanc1,1,10e-4,1000))
