""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# CoulWF.py:  Regular Coulomb scattering wave function

from scipy import special
# hypergeometric
from mpmath import *  
import matplotlib.pyplot as plt, numpy as np
from math import *

#     Initializations
f1 = np.zeros((10), complex)
Rea = np.zeros((10, 161), float)
zi = complex(0, 1.0)
mAu = 196.966569 * 931.494
mAlpha = 4.002602 * 931.494
Zau = 79
Zalph = 2
mu = mAlpha * mAu / (mAlpha + mAu)
# MeV-fm, E in MeV, r in fm
hbarc = 197.33  
Elab = 7.0
Ecom = Elab * mAu / (mAlpha + mAu)
vel = sqrt(Ecom * 2 / mu)
ka = sqrt(2.0 * mu * Ecom) / hbarc
# Coulomb parameter
etaco = Zalph * Zau * mu / (hbarc * ka * 137.0)  
expi = exp(-0.5 * etaco * pi)

# Main loop over r and i
i = 0  
for r in np.arange(0.1, 80.5, 0.5):
# -2ikr
    rho = complex(0, -2 * ka * r)  
# exp(ikr)
    expo = complex(cos(ka * r), sin(ka * r))  
    for L in range(0, 10):
# Arg gamma function
        a = L + 1.0 + etaco * zi  
# Hypergeometric
        sol = hyp1f1(a, 2 * L + 2.0, rho)  
        rhoL = (-rho) ** L
# Gamma(l+1+in)
        gam = special.gamma(a)  
        upar = rhoL * expo * sol * gam * expi / factorial(2 * L)
        f1[L] = upar / sqrt(vel)
# Real psi
        Rea[L, i] = f1.real[L]  
    i += 1

rr = np.arange(0.1, 80.5, 0.5)
plt.plot(rr, Rea[0, :], label="S")
plt.plot(rr, Rea[1, :], label="P", linewidth=2)
plt.plot(rr, Rea[2, :], label="D", linewidth=3)
plt.legend()
plt.xlabel("r (fermis)")
plt.title("Radial Coulmb Wave Functions $y_l(r)$ for $l = 0,1,2$")
plt.show()
