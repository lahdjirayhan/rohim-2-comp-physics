""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2011; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2011.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# DFT.py:  Discrete Fourier Transform
from visual import *
from visual.graph import *

# for the original signal
signgr = graph( x=0, y=0, width=600, height=250, title="Original signal y(t)= 3 cos(wt)+2 cos(3wt)+ cos(5wt) ", xtitle="x", ytitle="signal", xmax=2.0 * math.pi, xmin=0, ymax=7, ymin=-7, )
sigfig = gcurve(color=color.yellow, canvas=signgr)
# For the imaginary part of the transform
imagr = graph( x=0, y=250, width=600, height=250, title="Fourier transform imaginary part", xtitle="x", ytitle="Transf.Imag", xmax=10.0, xmin=-1, ymax=20, ymin=-70, )
# thin bars
impart = gvbars(delta=0.05, color=color.red, canvas=imagr)  
# for the real part of the transform
# # for you to do
# points for signal and transform
N = 10  
# global constants
Np = N  
signal = zeros((N + 1), float)
twopi = 2.0 * pi
sq2pi = 1.0 / sqrt(twopi)
h = twopi / N
# contains im. part of transform
dftimag = zeros((Np), float)  


# initial function
def f(signal):  
    step = twopi / N
    t = 0.0
    for i in range(0, N + 1):
        signal[i] = 3 * sin(t * t * t)
# plot function
        sigfig.plot(pos=(t, signal[i]))  
        t += step


# Discrete Fourier Transform
def fourier(dftimag):  
# over frequency
    for n in range(0, Np):  
# reset  variables
        imag = 0.0  
# loop for sums
        for k in range(0, N):  
            imag += signal[k] * sin((twopi * k * n) / N)
# imag. part transform
        dftimag[n] = -imag * sq2pi  
# to plot if not too small trnsf
        if dftimag[n] != 0:  
# plot bars
            impart.plot(pos=(n, dftimag[n]))  


f(signal)
fourier(dftimag)
print("hola")
for i in range(0, N):
    if abs(dftimag[i]) > 5:
        print(("i=", i, "dftimag ", dftimag[i]))
