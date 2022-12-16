""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# IntegGaussCall.py: N point Gaussian quadrature \int[a,b] f(x)dx

from numpy import *
from GaussPoints import GaussPoints

Npts = 10
Ans = 0
a = 0.0
b = 1.0
eps = 3.0e-14
w = zeros(2001, float)
# Arrays
x = zeros(2001, float)  


def f(x):
# Integrand
    return exp(x)  


#  eps: precison of pts
GaussPoints(Npts, a, b, x, w, eps)  
for i in range(0, Npts):
# Sum integrands
    Ans += f(x[i]) * w[i]  
print(("\n Npts =", Npts, ",   Ans =", Ans))
print((" eps =", eps, ", Error =", Ans - (exp(1) - 1)))
