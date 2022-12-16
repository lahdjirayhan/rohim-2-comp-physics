""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# DWT.py:  Discrete Wavelet Transform, Daubechies type

from visual import *
from visual.graph import *

sq3 = sqrt(3)
fsq2 = 4.0 * sqrt(2)
# N = 2^n
N = 1024  
c0 = (1 + sq3) / fsq2
# Daubechies 4 coeff
c1 = (3 + sq3) / fsq2  
c2 = (3 - sq3) / fsq2
c3 = (1 - sq3) / fsq2
# Display indicator
transfgr1 = None  
transfgr1 = None


# Chirp signal
def chirp(xi):  
    y = sin(60.0 * xi**2)
    return y


# DWT if sign >= 0, inverse if < 0
def daube4(f, n, sign):  
    global transfgr1, transfgr2
# Temporary
    tr = zeros((n + 1), float)  
    if n < 4:
        return
    mp = n / 2
# midpoint + 1
    mp1 = mp + 1  
# DWT
    if sign >= 0:  
        j = 1
        i = 1
        maxx = n / 2
# Scale
        if n > 128:  
            maxy = 3.0
            miny = -3.0
            Maxy = 0.2
            Miny = -0.2
# Fast rate
            speed = 50  
        else:
            maxy = 10.0
            miny = -5.0
            Maxy = 7.5
            Miny = -7.5
# Lower rate
            speed = 8  
        if transfgr1:
            transfgr1.canvas.visible = False
            transfgr2.canvas.visible = False
            del transfgr1
            del transfgr2
        transfgr1 = graph( x=0, y=0, width=600, height=400, title="Wavelet TF, down sample + low pass", xmax=maxx, xmin=0, ymax=maxy, ymin=miny, )
        transf = gvbars(delta=2.0 * n / N, color=color.cyan, canvas=transfgr1)
        transfgr2 = graph( x=0, y=400, width=600, height=400, title="Wavelet TF, down sample + high pass", xmax=2 * maxx, xmin=0, ymax=Maxy, ymin=Miny, )
        transf2 = gvbars(delta=2.0 * n / N, color=color.cyan, canvas=transfgr2)
        while j <= n - 3:
            rate(speed)
            tr[i] = c0 * f[j] + c1 * f[j + 1] + c2 * f[j + 2] + c3 * f[j + 3]
# c coefficients
            transf.plot(pos=(i, tr[i]))  
            tr[i + mp] = c3 * f[j] - c2 * f[j + 1] + c1 * f[j + 2] - c0 * f[j + 3]
            transf2.plot(pos=(i + mp, tr[i + mp]))
# d coefficents
            i += 1  
# downsampling
            j += 2  
# low-pass
        tr[i] = c0 * f[n - 1] + c1 * f[n] + c2 * f[1] + c3 * f[2]  
# c coefficients
        transf.plot(pos=(i, tr[i]))  
# hi
        tr[i + mp] = c3 * f[n - 1] - c2 * f[n] + c1 * f[1] - c0 * f[2]  
        transf2.plot(pos=(i + mp, tr[i + mp]))
# inverse DWT
    else:  
# low-pass
        tr[1] = c2 * f[mp] + c1 * f[n] + c0 * f[1] + c3 * f[mp1]  
# hi-pass
        tr[2] = c3 * f[mp] - c0 * f[n] + c1 * f[1] - c2 * f[mp1]  
        j = 3
        for i in range(1, mp):
            tr[j] = c2 * f[i] + c1 * f[i + mp] + c0 * f[i + 1] + c3 * f[i + mp1]
# upsample
            j += 1  
            tr[j] = c3 * f[i] - c0 * f[i + mp] + c1 * f[i + 1] - c2 * f[i + mp1]
            j += 1
            # upsampling
    for i in range(1, n + 1):
# copy TF to array
        f[i] = tr[i]  


# f -> TF
def pyram(f, n, sign):  
    if n < 4:
# too few data
        return  
# when to stop
    nend = 4  
# Transform
    if sign >= 0:  
        nd = n
# Downsample filtering
        while nd >= nend:  
            daube4(f, nd, sign)
            nd //= 2
# Inverse TF
    else:  
# Upsampling fix, thanks Pavel Snopok
        while nd <= n:  
            daube4(f, nd, sign)
            nd *= 2


# data vector
f = zeros((N + 1), float)  
# for chirp signal
inxi = 1.0 / N  
xi = 0.0
for i in range(1, N + 1):
# Function to TF
    f[i] = chirp(xi)  
    xi += inxi
# must be 2^m
n = N  
# TF
pyram(f, n, 1)  
# pyram(f, n,  - 1)                                  # Inverse TF
