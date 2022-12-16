""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# ScattSqWell.py: Quantum scattering from square well

import scipy.special, matplotlib.pyplot as plt, numpy as np
from math import *

a = 1
V = 15
E = 10
nLs = 10
Nin = 100
Nout = 100
alpha = np.sqrt(V + E)
beta = np.sqrt(E)
delta = np.zeros((nLs), float)
SigL = np.zeros((nLs, 200), float)


# Spherical Bessel ratio
def Gam(n, xx):  
    gamma = np.zeros((n), float)
    for nn in range(0, n):
        jn, jpr = scipy.special.sph_jn(nn, xx)
# gamma match psi outside-inside
    gamma = alpha * jpr / jn  
    return gamma


def phaseshifts(n, alpha, beta):
    gamm = Gam(n, alpha)
    num = np.zeros((n), float)
    den = np.zeros((n), float)
    jnb, jnpr = scipy.special.sph_jn(n, beta)
    ynb, yprb = scipy.special.sph_yn(n, beta)
    for i in range(0, n):
        num1 = gamm[i] * jnb[i]
        den1 = gamm[i] * ynb[i]
        num[i] = beta * jnpr[i] - num1
        den[i] = beta * yprb[i] - den1
        td = atan2(num[i], den[i])
        delta[i] = td
    return delta


def totalcrossect(n, alpha, beta):
    delta = phaseshifts(n, alpha, beta)
    suma = 0
    for i in range(0, n):
        suma = suma + (2 * i + 1) * (sin(delta[i])) ** 2
    return 4 * np.pi * suma / beta**2


def plotcross(alpha, beta):
    e = 0.0
# total crossection
    cross = np.zeros((200), float)  
    delta = phaseshifts(n, alpha, beta)
# energies
    en = np.zeros((200), float)  
    for i in range(1, 200):
        e = e + 100 / 300.0
        en[i] = e
        alpha = np.sqrt(V + e)
        beta = np.sqrt(e)
        cross[i] = totalcrossect(n, alpha, beta)
        for m in range(0, n):
            partot[m, i] = 4 * pi * (2 * m + 1) * (sin(delta[m])) ** 2 / beta**2
    f2 = plt.figure()
    ax2 = f2.add_subplot(111)
    plt.plot(en, cross, label="Total")
    plt.plot(en, partot[0, :], label="S ")
    plt.plot(en, partot[1, :], label="P ")
    plt.plot(en, partot[2, :], label="D")
    plt.plot(en, partot[3, :], label="E")
    plt.title("Total & Partial Cross Sections")
    plt.legend()
    plt.xlabel("Energy")


def diffcrossection():
    zz2 = np.zeros((n), complex)
    dcr = np.zeros((180), float)
# phaseshifts
    delta = phaseshifts(n, alpha, beta)  
# n partial waves
    for i in range(0, n):  
        cosd = cos(delta[i])
        sind = sin(delta[i])
        zz = complex(cosd, sind)
        zz2[i] = zz * sind
    for ang in range(0, 180):
        summ = 0.0
        radi = cos(ang * pi / 180.0)
#  partial wave loop
        for i in range(0, n):  
            poL = scipy.special.eval_legendre(i, radi)
            summ += (2 * i + 1) * zz2[i] * poL
        dcr[ang] = (summ.real**2 + summ.imag**2) / beta**2
    angu = np.arange(0, 180)
# plot separate figure
    f1 = plt.figure()  
    ax1 = f1.add_subplot(111)
# Semilog dsig/dw plot
    plt.semilogy(angu, dcr)  
    plt.xlabel("Scattering Angle")
    plt.title("Differential Cross Section")
    plt.grid()


# Compute Psi(<1) & Psi(>1)
def wavefunction():  
    delta = phaseshifts(n, alpha, beta)
    BL = np.zeros((n), complex)
# Psi(r<1), nLs
    Rin = np.zeros((n, Nin), float)  
    Rex = np.zeros((n, nexpts), float)
# BL for matching
    for i in range(0, 10):  
# SphBes
        jnb, jnpr = scipy.special.sph_jn(n, alpha)  
        jnf, jnfr = scipy.special.sph_jn(n, beta)
        ynb, yprb = r = scipy.special.sph_yn(n, beta)
        cosd = cos(delta[i])
        sind = sin(delta[i])
        zz = complex(cosd, -sind)
        num = jnb[i] * zz
        den = cosd * jnf[i] - sind * ynb[i]
# For wavefunction match
        BL[i] = num / den  
# Points increment
    intr = 1.0 / Nin  
# Internal Psi
    for i in range(0, n):  
        rin = intr
# PsiIn plot
        for ri in range(0, Nin):  
            alpr = alpha * rin
            jnint, jnintpr = scipy.special.sph_jn(n, alpr)
            Rin[i, ri] = rin * jnint[i]
            rin = rin + intr
    extr = 2.0 / nexpts
    for i in range(0, n):
        rex = 1.0
# PsiIn plot
        for rx in range(0, nexpts):  
            argu = beta * rex
            jnxt, jnintpr = scipy.special.sph_jn(n, argu)
            nxt, jnintpr = scipy.special.sph_yn(n, argu)
            factr = jnxt[i] * cos(delta[i]) - nxt[i] * sin(delta[i])
            fsin = sin(delta[i]) * factr
            fcos = cos(delta[i]) * factr
            Rex[i, rx] = rex * (fcos * BL.real[i] - fsin * BL.imag[i])
            rex = rex + extr
    ai = np.arange(0, 1, intr)
# PsiL to plot, CHANGE FOR OTHER WAVES
    nwaf = 0  
    f3 = plt.figure()
    ax3 = f3.add_subplot(111)
    plt.plot(ai, Rin[nwaf, :])
    ae = np.arange(1, 3, extr)
    plt.title("$\Psi(r<1), \ \ \Psi(r>1), \ \ \ell = 0$")
    plt.xlabel("$r$")
    plt.plot(ae, Rex[nwaf, :])


# Diff crossection
diffcrossection()  
# Total crossections
plotcross(alpha, beta)  
# Psi
wavefunction()  
