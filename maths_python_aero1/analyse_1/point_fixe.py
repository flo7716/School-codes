# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 08:39:45 2023

@author: flori
"""
from math import sqrt
from math import log
from math import exp
from math import sin
from math import cos
from math import asin,acos
from math import tan
from numpy import pi

def gexam1(x):
    return log(x+3)
def gexam2(x):
    return asin(8-x**3)
def gexam3(x):
    return 2+log(x)
def gexam4(x):
    return acos(log(x))

def gexam5(x):
    return(10**10-3*x**5-10**3*x**3)/10**4

def PointFixe(g,x0,epsilon,Nitermax):
    x=x0
    Niter=0
    while abs(g(x)-x)>epsilon and Niter<Nitermax:
        x=g(x)
        Niter+=1
    return(x,Niter) 

print(PointFixe(gexam1,0,10e-6,1000))
# print(PointFixe(gexam2,2.0,10e-6,1000))
print(PointFixe(gexam3,1.1,10e-6,1000))
# print(PointFixe(gexam4,1,10e-6,1000))
# print(PointFixe(gexam5,1,10e-6,1000))

# def g1(x):
#     return sqrt(8/exp(x))
# print(PointFixe(g1,0,1e-10,1000))


# # def g2(x):
# #     return asin(exp(x)-9)
# # print(PointFixe(g2,2,1e-10,1000))
# "Le point fixe ne marche pas pour f2"

# def g3(x):
#     return (2-x**3)/3
# print(PointFixe(g3,0,1e-10,1000))


# # def g4(x):
# #     return (9-x**3)/3
# # print(PointFixe(g4,0,1e-10,1000))
# "Le point fixe ne marche pas pour f4"

# def g5(x):
#     return (11-2*x)**(1/4)
# print(PointFixe(g5,0,1e-10,1000))

# def g6(x):
#     return 2*cos(x)+3
# print(PointFixe(g6,0,1e-10,1000))

# # def g7(x):
# #     return (-12-exp(x))/2
# # print(PointFixe(g7,0,1e-10,1000))
# "Le point fixe ne marche pas pour f7"

# def g8(x):
#     return -1/(2*tan(x))
# print(PointFixe(g8,1,1e-10,1000)) 

# # def g9(x):
# #     return (exp(x)-3)**(1/4)
# # print(PointFixe(g9,1,1e-10,1000))
# "Le point fixe ne marche pas pour f9"

# # def g10(x):
# #     return (17-x**4-2*x**2)/4
# # print(PointFixe(g10,1,1e-10,1000))
# "Le point fixe ne marche pas pour f10"

# # def g11(x):
# #     return (log(x**4+4)-5*exp(-x))
# # print(PointFixe(g11,1,1e-10,1000))
# "Le point fixe ne marche pas pour f11"


# def gexamblanc1(x):
#     return -(17-4*x-2*x**2)**(1/4)
# print(PointFixe(gexamblanc1,1,10e-4,1000)) 

# def gexamblanc2(x):
#     return log(10-log(x**2))/4
# print(PointFixe(gexamblanc2,2.4,10e-4,1000))
