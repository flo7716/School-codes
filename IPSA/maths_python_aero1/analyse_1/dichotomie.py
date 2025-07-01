from math import exp
from math import sin 
from math import cos 
from math import tan
from math import log
from numpy import linspace
from matplotlib.pyplot import plot,xlabel,ylabel,axhline,axvline,grid,title,show,legend


def f1(x):
    return x**2*exp(x)-8 



def Dichotomie(f,a0,b0,epsilon):
    a=a0
    b=b0
    n=0
    while abs(a-b)>epsilon:
        c=(a+b)/2
        if f(a)*f(c)>0:
            a=c 
            n=n+1
        else:
            b=c
            n=n 
    return(c,n)



print(Dichotomie(f1,0,1,1e-10))

# def f2(x):
#     return exp(x)+sin(x)-9
# print(Dichotomie(f2,0,2,1e-10))

# def f3(x):
#     return 3*x+x**3-2
# print(Dichotomie(f3,0,2,1e-10))

# def f4(x):
#     return 3*x+x**3-9 
# print(Dichotomie(f4,0,2,1e-10))

# def f5(x):
#     return x**4+2*x-11
# print(Dichotomie(f5,0,2,1e-10))

# def f6(x):
#     return x-2*cos(x)+3
# print(Dichotomie(f6,0,2,1e-10)) 

# def f7(x):
#     return exp(x)-2*x-12 
# print(Dichotomie(f7,0,2,1e-10))

# def f8(x):
#     return 2*tan(x)-x-1
# print(Dichotomie(f8,0,2,1e-10))

# def f9(x):
#     return exp(x)-x**4-3
# print(Dichotomie(f9,0,2,1e-10))

# def f10(x):
#     return x**4-2*x**2+4*x-17
# print(Dichotomie(f10,0,2,1e-10))

# def f11(x):
#     return exp(x)*log(x**4+4)-5
# print(Dichotomie(f11,0,2,1e-10)) 

# def f12(x):
#     return 2*x-sin(x)-1
# print(Dichotomie(f12,0,2,1e-10)) 

# def fexblanc1(x):
#     return x**4-2*x**2+4*x
# print(Dichotomie(fexblanc1,-4,2,1e-10))

# def fexblanc2(x):
#     return log(x**2)+4*exp(x)-10
# print(Dichotomie(fexblanc2,0.1,1.5,1e-10)) 


def fexam1(x):
    return exp(x)-x-3
print(Dichotomie(fexam1,0,2,10e-6))


def fexam2(x):
    return x**3+sin(x)-8
print(Dichotomie(fexam2,0,2,10e-6))

def fexam3(x):
    return x**2-log(x)-2
print(Dichotomie(fexam3,1.1,1.6,10e-6))

def fexam4(x):
    return cos(x)-log(x)
print(Dichotomie(fexam4,1,2,10e-6))

def fexam5(x):
    return 3*x**5+10**3*x**3+10**4*x-10**10
print(Dichotomie(fexam5,1,200,10e-6))
    
x=linspace(0.1,2,100)
y =[]
for xx in x:
    y.append(fexam3(xx))
plot(x,y)
axhline(y=0,color="red")
axvline(x=0,color="red")
grid(True)
xlabel("x")
ylabel("y")
title("graphe de f2")
show()


# def dichotomie_bis(f,a,b,epsilon):
#     a_n=[]
#     b_n=[]
#     if f(a)*f(b)<0:
#         n=0
#         while(abs(a-b)>epsilon):
#             c=(a+b)/2
#             if f(c)==0:
#                 return[a_n,b_n]
#             elif f(a)*f(c)>0:
#                 a=c
#             else:
#                 b=c
#             n=n+1
#             a_n.append(a)
#             b_n.append(b) 
#         return[a_n,b_n]
#     else:
#         print("Erreur. Vous devez changer les valeurs de a et b")
        
# borne_gauche=dichotomie_bis(f1,1,2,1e-10)[0]
# borne_droite=dichotomie_bis(f1,1,2,1e-10)[1]

# plot(range(1,len(borne_gauche)+1),borne_gauche,label="a_n")
# plot(range(1,len(borne_droite)+1),borne_droite,label="b_n")
# xlabel("n")
# legend()
# title("Evolution des bornes de l'intervalle")