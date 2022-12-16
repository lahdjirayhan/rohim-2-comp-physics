""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

#  FFT.py  FFT for complex numbers dtr[][2], returned in dtr

from vpython import *
from vpython import *

# 2**10
N = 1024  
signalgr = graph( x=0, y=0, width=500, height=250, title="Gaussian signal", xtitle="x", ytitle="y", xmax=25.0, xmin=-25.0, ymax=1, ymin=0, )
sigpl = gcurve(color=color.yellow, canvas=signalgr)
transgr = graph( x=0, y=250, width=500, height=250, title="FFT", xtitle="w", ytitle="W", xmax=1, xmin=-1.0, ymax=300, ymin=-300, )
trpl = gvbars(delta=0.01, color=color.cyan, canvas=transgr)
# Im
tipl = gvbars(delta=0.01, color=color.magenta, canvas=transgr)  
invgr = graph( x=0, y=500, width=500, height=250, title="inverse TF", xtitle="x", ytitle="y", xmax=25.0, xmin=-25.0, ymax=1, ymin=0, )
invpl = gcurve(color=color.yellow, canvas=invgr)
max = 2100
points = 1026
data = zeros((max), float)
dtr = zeros((points, 2), float)
# Width
sigma = 3.0  
foursig2 = 4.0 * sigma * sigma


def gaussian():
    psr = zeros((N + 1), float)
    psi = zeros((N + 1), float)
# -25 <= x <= 25
    len = 50.0  
    # m = N;
# Initial position
    a = 0.0  
# x increment
    dxx = 50.0 / N  
# left end
    xx = -0.5 * len  
# Space loop
    for n in range(0, N):  
        xma2 = (xx - a) * (xx - a) / foursig2
        psr[n] = exp(-xma2)
        psi[n] = 0.0
        dtr[n, 0] = psr[n]
        # data
        dtr[n, 1] = psi[n]
        sigpl.plot(pos=(xx, psr[n]))
        xx += dxx


# FFT of dtr[n,2]
def fft(nn, isign):  
    n = 2 * nn
    for i in range(0, nn + 1):
        j = 2 * i + 1
# Real dtr, odd data[j]
        data[j] = dtr[i, 0]  
# Imag dtr, even data[j+1]
        data[j + 1] = dtr[i, 1]  
# Data in bit reverse order
    j = 1  
    for i in range(1, n + 2, 2):
# Reorder equivalent to bit reverse
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
        mmax = 2
# Begin transform
    while (mmax - n) < 0:  
        istep = 2 * mmax
        theta = 6.2831853 / (1.0 * isign * mmax)
        sinth = sin(theta / 2.0)
        wstpr = -2.0 * sinth**2
        wstpi = sin(theta)
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
    for i in range(0, nn):
        j = 2 * i + 1
        dtr[i, 0] = data[j]
        dtr[i, 1] = data[j + 1]


# Power of 2
nn = 1024  
# -1 transform, +1 inverse transform
isign = -1  
# call function
gaussian()  
# Call FFT, use global dtr[][]
fft(nn, isign)  
# x from -25 to 25
L = 50.0  
# to transform k into -pi*N/L =< k=< pi*N/L
dk = 2.0 * pi / L  
for n in range(0, N):
    if n < N / 2:
        k = n * dk
        # positve k's (first half)
    else:
        k = (n - N) * dk
        # negative k's
    trpl.plot(pos=(k, dtr[n, 0]), canvas=transgr)
    if dtr[n, 1] > 0.1:
# dtr[n,1]= Im part is zero
        print((n, dtr[n, 1]))  
# no plot
    tipl.plot(pos=(k, dtr[n, 1]), canvas=transgr)  
# its bars should be magenta
print("Compute inverse FFT")  
isign = 1
fft(nn, isign)
# increment in x
dxx = 50.0 / N  
xx = -0.5 * L
# divide inverse by N to normalize
for n in range(0, N):  
    invpl.plot(pos=(xx, dtr[n, 0] / N), canvas=invgr)
    xx += dxx
print("Done")
