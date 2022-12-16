""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau,
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# Trap.py          trapezoid integration of t^2
#                A, B : endpoints,    N: points (not intervals)

from numpy import *

A = 0.0
B = 3.0
N = 100
h = (B - A) / (N - 1)
# initialization
sum = 0.0  

# trap rule
for i in range(1, N + 1):  
    t = A + (i - 1) * h
    if (i == 1) or (i == N):
# end with wt=h/2
        w = h / 2.0  
    else:
        w = h
    sum = sum + w * t * t

# print integral
print(("sum = ", sum))  
print("Enter and return a character to finish")
s = eval(input())
