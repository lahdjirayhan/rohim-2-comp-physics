""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Bisection.py: zero of f(x) via Bisection algorithm within [a,b]

from vpython import *

eps = 1e-3
Nmax = 100
a = 0.0
# Precision, [a,b]
b = 7.0  


def f(x):
# Your function here
    return 2 * math.cos(x) - x  


# Do not change
def Bisection(Xminus, Xplus, Nmax, eps):  
    for it in range(0, Nmax):
        x = (Xplus + Xminus) / 2.0
        print((" it =", it, " x = ", x, " f(x) =", f(x)))
        if f(Xplus) * f(x) > 0.0:
# Change x+ to x
            Xplus = x  
        else:
# Change x- to x
            Xminus = x  
# Converged?
        if abs(f(x)) < eps:  
            print(("\n Root found with precision eps = ", eps))
            break
        if it == Nmax - 1:
            print("\n No root after N iterations\n")
    return x


root = Bisection(a, b, Nmax, eps)
print((" Root =", root))
