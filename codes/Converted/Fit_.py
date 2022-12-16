""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2011; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2011.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# Fit.py     Linear least square fit; e.g. of matrix computation arrays

import pylab as p
from vpython import *
from numpy import *
from numpy.linalg import inv
from numpy.linalg import solve

# x range curve
t = arange(1.0, 2.0, 0.1)  
# Given x values
x = array([1.0, 1.1, 1.24, 1.35, 1.451, 1.5, 1.92])  
# Given y values
y = array([0.52, 0.8, 0.7, 1.8, 2.9, 2.9, 3.6])  
# Plot data in blue
p.plot(x, y, "bo")  
# error bar lenghts
sig = array([0.1, 0.1, 0.2, 0.3, 0.2, 0.1, 0.1])  
# Plot error bars
p.errorbar(x, y, sig)  
# Plot figure
p.title("Linear Least Square Fit")  
# Label axes
p.xlabel("x")  
p.ylabel("y")
# plot grid
p.grid(True)  
Nd = 7
# Initialize
A = zeros((3, 3), float)  
bvec = zeros((3, 1), float)
ss = sx = sxx = sy = sxxx = sxxxx = sxy = sxy = sxxy = 0.0

for i in range(0, Nd):
    sig2 = sig[i] * sig[i]
    ss += 1.0 / sig2
    sx += x[i] / sig2
    sy += y[i] / sig2
    rhl = x[i] * x[i]
    sxx += rhl / sig2
    sxxy += rhl * y[i] / sig2
    sxy += x[i] * y[i] / sig2
    sxxx += rhl * x[i] / sig2
    sxxxx += rhl * rhl / sig2

A = array([[ss, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxxx]])
bvec = array([sy, sxy, sxxy])

# Invert matrix
xvec = multiply(inv(A), bvec)  
# Matrix multiply
Itest = multiply(A, inv(A))  
print("\n x vector via inverse")
print((xvec, "\n"))
print("A*inverse(A)")
print((Itest, "\n"))

# Solve via elimination
xvec = solve(A, bvec)  
print("x Matrix via direct")
print((xvec, "end= "))
print("FitParabola Final Results\n")
# Desired fit
print("y(x) = a0 + a1 x + a2 x^2")  
print(("a0 = ", x[0]))
print(("a1 = ", x[1]))
print(("a2 = ", x[2], "\n"))
print(" i   xi     yi    yfit   ")
for i in range(0, Nd):
    s = xvec[0] + xvec[1] * x[i] + xvec[2] * x[i] * x[i]
    print((" %d %5.3f  %5.3f  %8.7f \n" % (i, x[i], y[i], s)))
# red line is the fit, red dots the fits at y[i]
curve = xvec[0] + xvec[1] * t + xvec[2] * t**2
points = xvec[0] + xvec[1] * x + xvec[2] * x**2
p.plot(t, curve, "r", x, points, "ro")
p.show()
