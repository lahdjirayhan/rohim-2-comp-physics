""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# CWT.py  Continuous Wavelet TF, a la Zlatko Dimcovic

import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D
from vpython import *

originalsignal = graph( x=0, y=0, width=600, height=200, title="Input Signal", xmin=0, xmax=12, ymin=-20, ymax=20, )
orsigraph = gcurve(color=color.yellow)
invtrgr = graph( x=0, y=200, width=600, height=200, title="Inverted Transform", xmin=0, xmax=12, ymin=-20, ymax=20, )
invtr = gcurve(x=list(range(0, 240)), canvas=invtrgr, color=color.green)
iT = 0.0
fT = 12.0
W = fT - iT
N = 240
h = W / N
noPtsSig = N
noS = 20
noTau = 90
iTau = 0.0
iS = 0.1
tau = iTau
s = iS

# Need *very* small s steps for high frequency;
dTau = W / noTau
dS = (W / iS) ** (1.0 / noS)
maxY = 0.001
# Signal
sig = zeros((noPtsSig), float)  


# Signal function
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
        yy = y[i]
        orsigraph.plot(pos=(t, yy))
        t += hs


# Form signal
signal(noPtsSig, sig)  
# Transform
Yn = zeros((noS + 1, noTau + 1), float)  


# Mother
def morlet(t, s, tau):  
    T = (t - tau) / s
    return sin(8 * T) * exp(-T * T / 2.0)


# Find wavelet TF
def transform(s, tau, sig):  
    integral = 0.0
    t = iT
    for i in range(0, len(sig)):
        t += h
        integral += sig[i] * morlet(t, s, tau) * h
    return integral / sqrt(s)


# Compute inverse
def invTransform(t, Yn):  
# Transform
    s = iS  
    tau = iTau
    recSig_t = 0
    for i in range(0, noS):
# Scale graph
        s *= dS  
        tau = iTau
        for j in range(0, noTau):
            tau += dTau
            recSig_t += dTau * dS * (s ** (-1.5)) * Yn[i, j] * morlet(t, s, tau)
    return recSig_t


print("working, finding transform, count 20")
for i in range(0, noS):
# Scaling
    s *= dS  
    tau = iT
    print(i)
    for j in range(0, noTau):
# Translate
        tau += dTau  
        Yn[i, j] = transform(s, tau, sig)
print("transform found")
for i in range(0, noS):
    for j in range(0, noTau):
        if Yn[i, j] > maxY or Yn[i, j] < -1 * maxY:
# Find max Y
            maxY = abs(Yn[i, j])  
tau = iT
s = iS
print("normalize")
for i in range(0, noS):
    s *= dS
    for j in range(0, noTau):
# Transform
        tau += dTau  
        Yn[i, j] = Yn[i, j] / maxY
    tau = iT
# Inverse TF
print("finding inverse transform")  
recSigData = "recSig.dat"
recSig = zeros(len(sig))
t = 0.0
print("count to 10")
kco = 0
j = 0
Yinv = Yn
for rs in range(0, len(recSig)):
# Find input signal
    recSig[rs] = invTransform(t, Yinv)  
    xx = rs / 20
    yy = 4.6 * recSig[rs]
    invtr.plot(pos=(xx, yy))
    t += h
    if kco % 24 == 0:
        j += 1
        print(j)
    kco += 1
x = list(range(1, noS + 1))
y = list(range(1, noTau + 1))
X, Y = p.meshgrid(x, y)


# Transform function
def functz(Yn):  
    z = Yn[X, Y]
    return z


Z = functz(Yn)
fig = p.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color="r")
ax.set_xlabel("s: scale")
ax.set_ylabel("Tau")
ax.set_zlabel("Transform")
p.show()

print("Done")
