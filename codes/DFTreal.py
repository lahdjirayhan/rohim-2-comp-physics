""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# DFTreal.py:  Discrete Fourier Transform using real numbers

from vpython import *

signgr = graph( x=0, y=0, width=600, height=250, title="Signal y(t)= 3 cos(wt)+2 cos(3wt)+ cos(5wt) ", xtitle="x", ytitle="signal", xmax=2.0 * math.pi, xmin=0, ymax=7, ymin=-7, )
sigfig = gcurve(color=color.yellow, canvas=signgr)
imagr = graph( x=0, y=250, width=600, height=250, title="Fourier transform imaginary part", xtitle="x", ytitle="Transf.Imag", xmax=10.0, xmin=-1, ymax=20, ymin=-25, )
impart = gvbars(delta=0.05, color=color.red, canvas=imagr)

N = 200
Np = N
signal = zeros((N + 1), float)
twopi = 2.0 * pi
sq2pi = 1.0 / sqrt(twopi)
h = twopi / N
# Im. transform
dftimag = zeros((Np), float)  


def f(signal):
    step = twopi / N
    t = 0.0
    for i in range(0, N + 1):
        signal[i] = 3 * sin(t * t * t)
        sigfig.plot(pos=(t, signal[i]))
        t += step


# DFT
def fourier(dftimag):  
    for n in range(0, Np):
        imag = 0.0
        for k in range(0, N):
            imag += signal[k] * sin((twopi * k * n) / N)
# Im transform
        dftimag[n] = -imag * sq2pi  
        if dftimag[n] != 0:
            impart.plot(pos=(n, dftimag[n]))


f(signal)
fourier(dftimag)
