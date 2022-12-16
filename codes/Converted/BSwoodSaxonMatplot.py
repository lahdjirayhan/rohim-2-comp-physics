""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# BSwoodSaxonMatplot.py: Bound state of Wood Saxon potential, wi Matplotlib

import matplotlib.pyplot as plt
import numpy as np
from math import *

dl = 1e-6
n = 1000
uL = np.zeros([1001], float)
uR = np.zeros([1001], float)
k2L = np.zeros([1001], float)
k2r = np.zeros([1001], float)
potV = np.zeros((n), float)
x = np.zeros((n), float)
xr = np.zeros((n), float)
psi = np.zeros((n), float)
imax = 100
xL0 = 0
# rightmost x point wave function
xr0 = 10.0  
h = 10.0 / n
amin = -5.5
amax = -2.0
e = amin
de = 0.01
uL[0] = 0.0
uL[1] = 0.00001
uR[0] = 0.0
uR[1] = 0.00001
im = 400
nL = im + 2
# for right wave function to mathch functions
nr = n - im + 1  
m = 5
istep = 0


# Potential :Woods Saxon
def V(x):  
# negative is the depth
    V0 = 50  
    a = 0.5
# R  = r0*A**(1/3), r0 = 1.25
    R = 1.25 * 4  
# potential
    v = -V0 / (1.0 + exp((x - R) / a))  
    return v


def plotV():
    i = 0
    for i in range(0, n):
        x[i] = i * h
        r = x[i]
        potV[i] = V(r)
        i += 1


# sets k2l=(sqrt(e-V))^2 and k2r
def setk2():  
    for i in range(0, n):
        x[i] = xL0 + i * h
        xr[i] = xr0 - i * h
        el = x[i]
        er = xr[i]
        k2L[i] = e - V(el)
        k2r[i] = e - V(er)


# Numerov algorithm can be used for
def numerov(n, h, k2, u):  
# left and right wave functions
    b = (h**2) / 12.0  
    for i in range(1, n - 1):
        u[i + 1] = ( 2 * u[i] * (1.0 - 5.0 * b * k2[i]) - (1.0 + b * k2[i - 1]) * u[i - 1] ) / (1.0 + b * k2[i + 1])


# finds k2L and k2r
setk2()  
# finds left wave function
numerov(nL, h, k2L, uL)  
# finds right wave function
numerov(nr, h, k2r, uR)  
# to Rescale  solution, at matching
fact = uR[nr - 2] / uL[im]  
for i in range(0, nL):
# rescale
    uL[i] = fact * uL[i]  
#  Log deriv
f0 = (uR[nr - 1] + uL[nL - 1] - uR[nr - 3] - uL[nL - 3]) / ( 2 * h * uR[nr - 2] )  


def normalize(istep):
    asum = 0
# to normalize wave function
    for i in range(0, n):  
        if i > im:
# add right wavefunction to left wave
            uL[i] = uR[n - i - 1]  
            asum = asum + uL[i] * uL[i]
    asum = sqrt(h * asum)
    for i in range(0, n):
        x[i] = xL0 + i * h
# next vertical line indicates match of wvfs.
        psi[i] = uL[i] / asum  
    if istep == 0:
        plotV()
        f3 = plt.figure()
        ax3 = f3.add_subplot(111)
        plt.title("Wavefunction First Iteration")
        plt.plot(x, psi)
        el = plt.axvline(x=4, color="r")
        plt.xlabel("r (fm)")
        plt.ylabel("Potential and Wavefunction")
        plt.plot(x, potV)
    if istep == 1:
        plotV()
        f4 = plt.figure()
        ax4 = f4.add_subplot(111)
        plt.title("Wavefunction Second Iteration")
        plt.plot(x, psi)
        plt.plot(x, potV)
        el = plt.axvline(x=4, color="r")
        plt.xlabel("r (fm)")
        plt.ylabel("Potential and Wavefunction")
    if istep == 15:
        plotV()
        f4 = plt.figure()
        ax4 = f4.add_subplot(111)
        plt.title("Wavefunction 15th Iteration")
        plt.plot(x, psi)
        plt.plot(x, potV)
        el = plt.axvline(x=4, color="r")
        plt.xlabel("r (fm)")
        plt.ylabel("Potential and Wavefunction")


# bisection algorithm begins
while abs(de) > dl and istep < imax:  
# guessed root
    e1 = e  
# half interval
    e = (amin + amax) / 2  
    for i in range(0, n):
        k2L[i] = k2L[i] + e - e1
        k2r[i] = k2r[i] + e - e1
    im = 500
    nl = im + 2
    nr = n - im + 1
# Find wavefuntions for new k2l,k2r
    numerov(nl, h, k2L, uL)  
    numerov(nr, h, k2r, uR)
    fact = uR[nr - 2] / uL[im]
    for i in range(0, nL):
        uL[i] = fact * uL[i]
# Log deriv.
    f1 = (uR[nr - 1] + uL[nl - 1] - uR[nr - 3] - uL[nl - 3]) / ( 2 * h * uR[nr - 2] )  
# bisection localize root
    if f0 * f1 < 0:  
# searches in ewhat side is root
        amax = e  
        de = amax - amin
    else:
        amin = e
        de = amax - amin
        f0 = f1
# find new wavefunctions
    normalize(istep)  
    print(("iteration number =", istep, "Energy =", e))
    istep = istep + 1
plt.show()
