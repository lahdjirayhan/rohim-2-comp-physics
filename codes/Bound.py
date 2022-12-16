""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Bound.py: Bound state solutn of Lippmann-Schwinger equation in p space

from vpython import *
from numpy import *
from numpy.linalg import *

min1 = 0.0
max1 = 200.0
u = 0.5
b = 10.0


def gauss(npts, a, b, x, w):
    pp = 0.0
    m = (npts + 1) // 2
# Accuracy: ADJUST!
    eps = 3.0e-10  

    for i in range(1, m + 1):
        t = cos(math.pi * (float(i) - 0.25) / (float(npts) + 0.5))
        t1 = 1
        while (abs(t - t1)) >= eps:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, npts + 1):
                p3 = p2
                p2 = p1
                p1 = ((2 * j - 1) * t * p2 - (j - 1) * p3) / j
            pp = npts * (t * p1 - p2) / (t * t - 1.0)
            t1 = t
            t = t1 - p1 / pp
        x[i - 1] = -t
        x[npts - i] = t
        w[i - 1] = 2.0 / ((1.0 - t * t) * pp * pp)
        w[npts - i] = w[i - 1]
    for i in range(0, npts):
        x[i] = x[i] * (b - a) / 2.0 + (b + a) / 2.0
        w[i] = w[i] * (b - a) / 2.0


for M in range(16, 32, 8):
    z = [-1024, -512, -256, -128, -64, -32, -16, -8, -4, -2]
    for lmbda in z:
# Hamiltonian
        A = zeros((M, M), float)  
# Eigenvalues, potential
        WR = zeros((M), float)  
        k = zeros((M), float)
        w = zeros((M), float)
        # Pts & wts
# Call gauss points
        gauss(M, min1, max1, k, w)  
# Set Hamiltonian
        for i in range(0, M):  
            for j in range(0, M):
                VR = lmbda / 2 / u * sin(k[i] * b) / k[i] * sin(k[j] * b) / k[j]
                A[i, j] = 2.0 / math.pi * VR * k[j] * k[j] * w[j]
                if i == j:
                    A[i, j] += k[i] * k[i] / 2 / u
        Es, evectors = eig(A)
# Real eigenvalues
        realev = Es.real  
        for j in range(0, M):
            if realev[j] < 0:
                print((" M (size), lmbda, ReE = ", M, " ", lmbda, " ", realev[j]))
                break
