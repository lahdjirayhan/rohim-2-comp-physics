""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# CWT_zd.java  Continuous Wavelet Transform. Written by Zlatko Dimcovic

"""Different wavelets (middle) used during transform, and transform (top) 
for each wavelet. Then wavelet translated and scaled."""

from visual import *
from visual.graph import *

N = 240
transfgr = canvas(x=0, y=0, width=600, height=200, title="Transform, not normalized")
transf = curve(x=list(range(0, 90)), canvas=transfgr, color=color.cyan)
wavlgr = canvas( x=0, y=200, width=600, height=200, title="Morlet Wavelet at different scales, up to s=12.0", )
wavelet = curve(x=list(range(0, N)), canvas=wavlgr, color=color.yellow)
invtrgr = canvas(x=0, y=400, width=600, height=200, title="Inverse TF, not normalized")
invtr = curve(x=list(range(0, N)), canvas=invtrgr, color=color.green)
wvlabel = label(pos=vector(0, -50,0), text="s=", box=0, canvas=wavlgr)

iT = 0.0
fT = 12.0
# i,f times
W = fT - iT  
h = W / N
# Steps
noPtsSig = N
noS = 30
# of pts
noTau = 90  
iTau = 0.0
iS = 0.1
tau = iTau
s = iS

""" Need *very* small s steps for high-frequency, but only if s is small
Thus increment s by multiplying by number close enough to 1 """

dTau = W / noTau
dS = (W / iS) ** (1.0 / noS)
# Signal
sig = zeros((noPtsSig), float)  
# Transform
Y = zeros((noS, noTau), float)  
maxY = 0.001


# The signal
def signal(noPtsSig, y):  
    t = 0.0
    hs = W / noPtsSig
    t1 = W / 6.0
    t2 = 4.0 * W / 6.0
    for i in range(0, noPtsSig):
        if t >= iT and t <= t1:
            y[i] = sin(2 * pi * t)
        elif t >= t1 and t <= t2:
            y[i] = 5.0 * sin(2 * pi * t) + 10.0 * sin(4 * pi * t)
        elif t >= t2 and t <= fT:
            y[i] = ( 2.5 * sin(2 * pi * t) + 6.0 * sin(4 * pi * t) + 10.0 * sin(6 * pi * t) )
        else:
            print("In signal(...) : t out of range.")
            sys.exit(1)
        t += hs


signal(noPtsSig, sig)


# Mother
def morlet(t, s, tau):  
    T = (t - tau) / s
    return sin(8 * T) * exp(-T * T / 2.0)


def transform(s, tau, sig, j):
    integral = 0.0
# "initial time" = class variable
    t = 0.0  
    if j % 2 == 0:
        wvlabel.text = "s=%5.3f" % s
    for i in range(0, len(sig)):
        t += h
        yy = morlet(t, s, tau)
        if j % 2 == 0:
# the transform are drawn
            wavelet.x[i] = 110.0 / 3 * t - 240  
            wavelet.y[i] = 40.0 * yy
        integral += sig[i] * yy * h
        output = integral / sqrt(s)
    return output


# given the transform (from previous steps)
def invTransform(t, Y):  
# computes original signal
    s = iS  
    tau = iTau
    recSig_t = 0
    for i in range(0, noS):
        s *= dS
        tau = iTau
        for j in range(0, noTau):
            tau += dTau
            recSig_t += dTau * dS * (s ** (-1.5)) * Y[i, j] * morlet(t, s, tau)
    return recSig_t


print("working, finding transform")
for i in range(0, noS):
    rate(150)
# Scaling s
    s *= dS  
    tau = 0.0
    for j in range(0, noTau):
# Translation
        tau += dTau  
        Y[i, j] = transform(s, tau, sig, i)
        transf.x[j] = 40.0 / 3.0 * tau - 80
        transf.y[j] = 4.0 * Y[i, j]
print("transform found")
# Inverse TF
print("finding inverse transform")  
recSigData = "recSig.dat"
# Same resolution
recSig = zeros(len(sig))  
t = 0.0
kco = 0
j = 0
# with inverse transform
for rs in range(0, len(recSig)):  
# find the original signal
    recSig[rs] = invTransform(t, Y)  
# not normalized
    t += h  
    invtr.x[rs] = rs * 2.0 - 220
    invtr.y[rs] = 1.5 * recSig[rs]

print("nDone")
