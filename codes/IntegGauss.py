"""Dirichlet boundary conditions surrounding four walls 
 Domain dimensions: WxH, with 2 triangles per square  
 Based on FEM2DL_Box Matlab program in Polycarpou, Intro to the Finite 
 Element Method in Electromagnetics, Morgan & Claypool (2006) """

# IntegGauss.py: Gaussian quadrature generator of pts & wts

from numpy import *
from sys import version

# Numb intervals
max_in = 11  
vmin = 0.0
# Int ranges
vmax = 1.0  
# Euler's const
ME = 2.7182818284590452354e0  
w = zeros((2001), float)
x = zeros((2001), float)


# The integrand
def f(x):  
    return exp(-x)


def gauss(npts, job, a, b, x, w):
    m = i = j = t = t1 = pp = p1 = p2 = p3 = 0.0
# Accuracy: ******ADJUST THIS*******!
    eps = 3.0e-14  
    m = int((npts + 1) / 2)
    for i in range(1, m + 1):
        t = cos(math.pi * (float(i) - 0.25) / (float(npts) + 0.5))
        t1 = 1
        while (abs(t - t1)) >= eps:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, npts + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * float(j) - 1) * t * p2 - (float(j) - 1.0) * p3) / ( float(j) )
            pp = npts * (t * p1 - p2) / (t * t - 1.0)
            t1 = t
            t = t1 - p1 / pp
        x[i - 1] = -t
        x[npts - i] = t
        w[i - 1] = 2.0 / ((1.0 - t * t) * pp * pp)
        w[npts - i] = w[i - 1]
    if job == 0:
        for i in range(0, npts):
            x[i] = x[i] * (b - a) / 2.0 + (b + a) / 2.0
            w[i] = w[i] * (b - a) / 2.0
    if job == 1:
        for i in range(0, npts):
            xi = x[i]
            x[i] = a * b * (1.0 + xi) / (b + a - (b - a) * xi)
            w[i] = ( w[i] * 2.0 * a * b * b / ((b + a - (b - a) * xi) * (b + a - (b - a) * xi)) )
    if job == 2:
        for i in range(0, npts):
            xi = x[i]
            x[i] = (b * xi + b + a + a) / (1.0 - xi)
            w[i] = w[i] * 2.0 * (a + b) / ((1.0 - xi) * (1.0 - xi))


def gaussint(no, min, max):
    quadra = 0.0
# Returns pts & wts
    gauss(no, 0, min, max, x, w)  
    for n in range(0, no):
# Calculate integral
        quadra += f(x[n]) * w[n]  
    return quadra


for i in range(3, max_in + 1, 2):
    result = gaussint(i, vmin, vmax)
    print((" i ", i, " err ", abs(result - 1 + 1 / ME)))
print("Enter and return any character to quit")
