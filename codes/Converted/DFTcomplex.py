""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# DFTcomplex.py:  Discrete Fourier Transform wi Python complex math

from vpython import *
from vpython import *
# Complex math
import cmath  

N = 100
twopi = 2.0 * pi
h = twopi / N
sq2pi = 1.0 / sqrt(twopi)
y = zeros(N + 1, float)
# Arrays
Ycomplex = zeros(N, complex)  

SignalGraph = graph( x=0, y=0, width=600, height=250, title="Signal y(t)", xtitle="x", ytitle="y(t)", xmax=2.0 * math.pi, xmin=0, ymax=30, ymin=-30, )
SignalCurve = gcurve(color=color.yellow, canvas=SignalGraph)
TransformGraph = graph( x=0, y=250, width=600, height=250, title="Im Y(omega)", xtitle="x", ytitle="Im Y(omega)", xmax=10.0, xmin=-1, ymax=100, ymin=-250, )
TransformCurve = gvbars(delta=0.05, color=color.red, canvas=TransformGraph)


# Signal
def Signal(y):  
    h = twopi / N
    x = 0.0
    for i in range(0, N + 1):
        y[i] = 30 * cos(x) + 60 * sin(2 * x) + 120 * sin(3 * x)
# Plot
        SignalCurve.plot(pos=(x, y[i]))  
        x += h


# DFT
def DFT(Ycomplex):  
    for n in range(0, N):
        zsum = complex(0.0, 0.0)
        for k in range(0, N):
# Complex exponent
            zexpo = complex(0, twopi * k * n / N)  
            zsum += y[k] * exp(-zexpo)
        Ycomplex[n] = zsum * sq2pi
        if Ycomplex[n].imag != 0:
            TransformCurve.plot(pos=(n, Ycomplex[n].imag))


# Generate signal
Signal(y)  
# Transform signal
DFT(Ycomplex)  
