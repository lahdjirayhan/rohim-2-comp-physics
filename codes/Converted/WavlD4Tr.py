""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

""" Uses global variables nedeed to perform wavelet or inverse 
 Wavelet Discrete Transform, Daubechies type"""

from visual import *
from visual.graph import *

N = 1024
# number of data points must be, 4,8,16,32,...,1024..
"""  
Function tht returns  the chirp signal sin(60 t*t)
generally for 0<=t <=0 (selected in main program)
xi is the variable time
"""
sq3 = math.sqrt(3)
fsq2 = 4.0 * math.sqrt(2)
# Daubechies 4 coefficents
c0 = (1.0 + sq3) / fsq2  
c1 = (3.0 + sq3) / fsq2
c2 = (3.0 - sq3) / fsq2
c3 = (1.0 - sq3) / fsq2


def chirp(xi):
    y = math.sin(60.0 * xi**2)
    return y


"""            
Continues the Discret Wavelet Transform, Daubechies 4
or the inverse Daubechies 4 transform
sign:>=0 for DWT,
sign:<0 for inverse transform
"""


def daube4(f, n, sign):
# temporary variable
    tr = zeros((n + 1), float)  
    # print "n",n
    if n < 4:
        return
# midpoint of array
    mp = n / 2  
# midpoint plus one
    mp1 = mp + 1  
# DWT
    if sign >= 0:  
        j = 1
        i = 1
        maxx = n / 2
# appropiate scales
        if n > 128:  
            maxy = 3.0
            miny = -3.0
            Maxy = 0.2
            Miny = -0.2
# fast rate
            speed = 50  
        else:
            maxy = 10.0
            miny = -5.0
            Maxy = 7.5
            Miny = -7.5
# for lower rate
            speed = 8  
        transfgr1 = graph( x=0, y=0, width=600, height=400, title="Wavelet Transform, down sampling, Low pass filters", xmax=maxx, xmin=0, ymax=maxy, ymin=miny, )
        # notice that the width of the bars (delta)  changes with scale
        transf = gvbars(delta=2.0 * n / N, color=color.cyan, canvas=transfgr1)
        transfgr2 = graph( x=0, y=400, width=600, height=400, title="Wavelet Transform, down sampling, High pass filters", xmax=2 * maxx, xmin=0, ymax=Maxy, ymin=Miny, )
        transf2 = gvbars(delta=2.0 * n / N, color=color.cyan, canvas=transfgr2)

        while j <= n - 3:
            rate(speed)

# low-pass
            tr[i] = ( c0 * f[j] + c1 * f[j + 1] + c2 * f[j + 2] + c3 * f[j + 3] )  
# c coefficients
            transf.plot(pos=(i, tr[i]))  
# high-pass
            tr[i + mp] = ( c3 * f[j] - c2 * f[j + 1] + c1 * f[j + 2] - c0 * f[j + 3] )  
            transf2.plot(pos=(i + mp, tr[i + mp]))
# d coefficents
            i += 1  
# downsampling here
            j += 2  
        # l ast data
# low-pass filter
        tr[i] = c0 * f[n - 1] + c1 * f[n] + c2 * f[1] + c3 * f[2]  
# c coefficients
        transf.plot(pos=(i, tr[i]))  
# high-pass filter
        tr[i + mp] = ( c3 * f[n - 1] - c2 * f[n] + c1 * f[1] - c0 * f[2] )  
        transf2.plot(pos=(i + mp, tr[i + mp]))
# inverse DWT
    else:  
# low-pass first one
        tr[1] = c2 * f[mp] + c1 * f[n] + c0 * f[1] + c3 * f[mp1]  
# high-pass 2nd one
        tr[2] = c3 * f[mp] - c0 * f[n] + c1 * f[1] - c2 * f[mp1]  

        for i in range(1, mp):
            if i == 1:
                j = 3
# low-pass
            tr[j] = ( c2 * f[i] + c1 * f[i + mp] + c0 * f[i + 1] + c3 * f[i + mp1] )  
# upsamplig  c coefficients
            j += 1  
# high-pass
            tr[j] = ( c3 * f[i] - c0 * f[i + mp] + c1 * f[i + 1] - c2 * f[i + mp1] )  
            j += 1
            # upsampling  d coefficients
    for i in range(1, n + 1):
# copy transform in data array
        f[i] = tr[i]  


"""  
Calls wavelet transform routine daube4  (Daubechies 4 wavelet D4)
with sign=1 to perform the D4 discrete Wavelet transform
or with sign=-1 the inverse D4 wavelet trnsform
f the input data, it hs to have 2**n data (4,8,16,32,...)
"""


def pyram(f, n, sign):
    # Discrete wavelet transform. Replaces f by its wavelet transform
    if n < 4:
# too few data
        return  
    nend = 4
    # this variable indicates when to stop the loop
    # or can be selected as 512,256,128,64,..,4 t
# Wavelet transform
    if sign >= 0:  
        nd = n
# Performs filtering operations downsampling
        while nd >= nend:  
            daube4(f, nd, sign)
            nd /= 2
# Inverse wavelet transform
    else:  
        nd = 4
# perform upsampling
        while nd <= n + 1:  
            daube4(f, nd, sign)
            nd *= 2


# data vector
f = zeros((N + 1), float)  
# for the chirp signal interval 0=<t <=1.0
inxi = 1.0 / N  
# selects initial data
xi = 0.0
for i in range(1, N + 1):
# change if you use another function
    f[i] = chirp(xi)  
    xi += inxi
    # different of chirp or if need for next 2 lines
    # f[i] = 0.0;         if instead of chirp to find formation of Wavelet
    # f[5] = 1.0;         used with this line too
    # w.println(" "+xi+" "+f[i]+" ")           # copy in file "indata.dat"
# total number of datapoints it must be 4,8,16,32,...,1024,...
n = N  
# Discret Wavelet Transform
pyram(f, n, 1)  
# pyram(f,n,-1)                                             # i nverse DWT
