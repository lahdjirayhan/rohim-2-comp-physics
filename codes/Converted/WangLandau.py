"""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# WangLandau.py: Wang Landau algorithm for 2-D spin system

""" Author in Java: Oscar A. Restrepo, 
 Universidad de Antioquia, Medellin, Colombia
 Each time fac changes, a new histogrm is generated.
 Only the first Histogram plotted to reduce computational time"""
from vpython import *
import random
from vpython import *

L = 8
N = L * L

# Set up graphics
entgr = graph( x=0, y=0, width=500, height=250, title="Density of States", xtitle="E/N", ytitle="log g(E)", xmax=2.0, xmin=-2.0, ymax=45, ymin=0, )
entrp = gcurve(color=color.yellow, canvas=entgr)
energygr = graph( x=0, y=250, width=500, height=250, title="E vs T", xtitle="T", ytitle="U(T)/N", xmax=8.0, xmin=0, ymax=0.0, ymin=-2.0, )
energ = gcurve(color=color.cyan, canvas=energygr)
histogr = canvas( x=0, y=500, width=500, height=300, title="1st histogram: H(E) vs. E/N, corresponds to log(f) = 1", )
histo = curve(x=list(range(0, N + 1)), color=color.red, canvas=histogr)
xaxis = curve(pos=[(-N, -10), (N, -10)])
minE = label(text=" - 2", pos=vector(-N + 3, -15,0), box=0)
maxE = label(text="2", pos=vector(N - 3, -15,0), box=0)
zeroE = label(text="0", pos=vector(0, -15,0), box=0)
ticm = curve(pos=[(-N, -10), (-N, -13)])
tic0 = curve(pos=[(0, -10), (0, -13)])
ticM = curve(pos=[(N, -10), (N, -13)])
enr = label(text="E/N", pos=vector(N / 2, -15,0), box=0)

# Grid size, spins
sp = zeros((L, L))  
hist = zeros((N + 1))
# Histograms
prhist = zeros((N + 1))  
# Entropy = log g(E)
S = zeros((N + 1), float)  


def iE(e):
    return int((e + 2 * N) / 4)


def IntEnergy():
    exponent = 0.0
# Select lambda max
    for T in arange(0.2, 8.2, 0.2):  
        Ener = -2 * N
# Initialize
        maxL = 0.0  
        for i in range(0, N + 1):
            if S[i] != 0 and (S[i] - Ener / T) > maxL:
                maxL = S[i] - Ener / T
                Ener = Ener + 4
        sumdeno = 0
        sumnume = 0
        Ener = -2 * N
        for i in range(0, N):
            if S[i] != 0:
                exponent = S[i] - Ener / T - maxL
            sumnume += Ener * exp(exponent)
            sumdeno += exp(exponent)
            Ener = Ener + 4.0
# internal energy U(T)/N
        U = sumnume / sumdeno / N  
        energ.plot(pos=(T, U))


# Wang - Landau sampling
def WL():  
# initial values for Histogram
    Hinf = 1.0e10  
    Hsup = 0.0
# tolerance, stops the algorithm
    tol = 1.0e-3  
    ip = zeros(L)
# BC R or down, L or up
    im = zeros(L)  
# Initialize histogram
    height = abs(Hsup - Hinf) / 2.0  
# about average of histogram
    ave = (Hsup + Hinf) / 2.0  
    percent = height / ave
    for i in range(0, L):
        for j in range(0, L):
# Initial spins
            sp[i, j] = 1  
    for i in range(0, L):
        ip[i] = i + 1
# Case plus, minus
        im[i] = i - 1  
    ip[L - 1] = 0
# Borders
    im[0] = L - 1  
# Initialize energy
    Eold = -2 * N  
    for j in range(0, N + 1):
# Entropy initialized
        S[j] = 0  
    iter = 0
    fac = 1
    while fac > tol:

# Select random spin
        i = int(N * random.random())  
        xg = i % L
        # Must be i//L, not i/L for Python 3:
# Localize x, y, grid point
        yg = i // L  
# Change energy
        Enew = ( Eold + 2 * (sp[ip[xg], yg] + sp[im[xg], yg] + sp[xg, ip[yg]] + sp[xg, im[yg]]) * sp[xg, yg] )  
        deltaS = S[iE(Enew)] - S[iE(Eold)]
        if deltaS <= 0 or random.random() < exp(-deltaS):
            Eold = Enew
# Flip spin
            sp[xg, yg] *= -1  
        S[iE(Eold)] += fac
        # Change entropy
# Check flatness every 10000 sweeps
        if iter % 10000 == 0:  
            for j in range(0, N + 1):
                if j == 0:
                    Hsup = 0
# Initialize new histogram
                    Hinf = 1e10  
                if hist[j] == 0:
# Energies never visited
                    continue  
                if hist[j] > Hsup:
                    Hsup = hist[j]
                if hist[j] < Hinf:
                    Hinf = hist[j]
            height = Hsup - Hinf
            ave = Hsup + Hinf
# 1.0 to make it float number
            percent = 1.0 * height / ave  
# Histogram flat?
            if percent < 0.3:  
                print((" iter ", iter, "   log(f) ", fac))
                for j in range(0, N + 1):
# to plot
                    prhist[j] = hist[j]  
# Save hist
                    hist[j] = 0  
# Equivalent to log(sqrt(f))
                fac *= 0.5  
        iter += 1
# Change histogram, add 1, update
        hist[iE(Eold)] += 1  
# just show the first histogram
        if fac >= 0.5:  
            # Speed up by using array calculations:
            histo.x = 2.0 * arange(0, N + 1) - N
            histo.y = 0.025 * hist - 10


deltaS = 0.0
# not always the same
print("wait because iter > 13 000 000")  
# Call Wang Landau algorithm
WL()  
deltaS = 0.0
for j in range(0, N + 1):
    rate(150)
    order = j * 4 - 2 * N
    deltaS = S[j] - S[0] + log(2)
    if S[j] != 0:
# plot entropy
        entrp.plot(pos=(1.0 * order / N, deltaS))  
IntEnergy()
print("Done")
