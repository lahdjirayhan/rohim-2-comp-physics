""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# NewtonCall.py    Newton Search with central difference

from math import cos

x0 = 1111.0
dx = 3.0e-4
eps = 0.002
Nmax = 100
# Parameters


def f(x):
# Function
    return 2 * cos(x) - x  


def NewtonR(x, dx, eps, Nmax):
    for it in range(0, Nmax + 1):
        F = f(x)
# Converged?
        if abs(F) <= eps:  
            print(("\n Root found, f(root) =", F, ", eps = ", eps))
            break
        print(("Iteration # = ", it, " x = ", x, " f(x) = ", F))
# Central diff
        df = (f(x + dx / 2) - f(x - dx / 2)) / dx  
        dx = -F / df
# New guess
        x += dx  
    if it == Nmax + 1:
        print(("\n Newton Failed for Nmax =", Nmax))
    return x
