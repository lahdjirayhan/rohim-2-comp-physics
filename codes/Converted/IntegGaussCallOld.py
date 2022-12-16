""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""


# IntegGauss.py: N point Gaussian quadrature \int_0^1 exp(x) dx

from numpy import *
from sys import version
from GaussPoints import GaussPoints

# Numb points
Npts = 10  
a = 0.0
# Int ranges
b = 1.0  
# Precision desired
eps = 3.0e-14  
w = zeros((2001), float)
x = zeros((2001), float)


# Place integrand here
def f(x):  
    return exp(x)


# Sum integrand*weight
def GaussInt(Npts, a, b, eps):  
    quadra = 0.0
# Get pts, eps = precison
    GaussPoints(Npts, a, b, x, w, eps)  
    for i in range(0, Npts):
# Sum weighted integrands
        quadra += f(x[i]) * w[i]  
    return quadra


Ans = GaussInt(Npts, a, b, eps)
print()
print(("Npts =", Npts, "Ans =", Ans))
print(("eps =", eps, "Sum-Analytic =", Ans - (exp(1) - 1)))
