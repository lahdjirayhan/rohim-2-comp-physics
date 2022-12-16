""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# FFTmod.py:  FFT for complex numbers in dtr[][2], returned in dtr

# from sys import version
from numpy import *  

max = 2100
points = 1026
# Power of 2
N = 16  
# -1, 1 TF, inverse TF
isign = -1  
data = zeros((max), float)
dtr = zeros((points, 2), float)


# FFT of dtr[n,2]
def FFT(N, isign):  
    n = 2 * N
    for i in range(0, N + 1):
        j = 2 * i + 1
# Real dtr, odd data[j]
        data[j] = dtr[i, 0]  
# Imag dtr, even data[j+1]
        data[j + 1] = dtr[i, 1]  
# Place reverse order
    j = 1  
    for i in range(1, n + 2, 2):
        if (i - j) < 0:
            tempr = data[j]
            tempi = data[j + 1]
            data[j] = data[i]
            data[j + 1] = data[i + 1]
            data[i] = tempr
            data[i + 1] = tempi
        m = n / 2
        while m - 2 > 0:
            if (j - m) <= 0:
                break
            j = j - m
            m = m / 2
        j = j + m
    print("\n Bit-Reversed Input Data ")
    for i in range(1, n + 1, 2):
        print(("%2d data[%2d] %9.5f " % (i, i, data[i])))
    mmax = 2
# Begin transform
    while (mmax - n) < 0:  
        istep = 2 * mmax
        theta = 6.2831853 / (isign * mmax)
        sinth = math.sin(theta / 2.0)
        wstpr = -2.0 * sinth**2
        wstpi = math.sin(theta)
        wr = 1.0
        wi = 0.0
        for m in range(1, mmax + 1, 2):
            for i in range(m, n + 1, istep):
                j = i + mmax
                tempr = wr * data[j] - wi * data[j + 1]
                tempi = wr * data[j + 1] + wi * data[j]
                data[j] = data[i] - tempr
                data[j + 1] = data[i + 1] - tempi
                data[i] = data[i] + tempr
                data[i + 1] = data[i + 1] + tempi
            tempr = wr
            wr = wr * wstpr - wi * wstpi + wr
            wi = wi * wstpr + tempr * wstpi + wi
        mmax = istep
    for i in range(0, N):
        j = 2 * i + 1
        dtr[i, 0] = data[j]
        dtr[i, 1] = data[j + 1]


print("\n        Input")
print("  i   Re part   Im  part")
# Form array
for i in range(0, N):  
# Real part
    dtr[i, 0] = 1.0 * i  
# Im part
    dtr[i, 1] = 1.0 * i  
    print((" %2d %9.5f %9.5f" % (i, dtr[i, 0], dtr[i, 1])))
# Call FFT, use global dtr[][]
FFT(N, isign)  
print("\n    Fourier Transform \n  i      Re      Im    ")
for i in range(0, N):
    print((" %2d  %9.5f  %9.5f " % (i, dtr[i, 0], dtr[i, 1])))
print("Enter and return any character to quit")
