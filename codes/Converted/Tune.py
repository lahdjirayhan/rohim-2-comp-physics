""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2011; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2011.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# Tune.py Basic tuning program showing memory allocation

import datetime
from numpy import zeros
from math import sqrt, pow

Ldim = 251
iter = 0
step = 0.0
diag = zeros((Ldim, Ldim), float)
coef = zeros((Ldim), float)
sigma = zeros((Ldim), float)
ham = zeros((Ldim, Ldim), float)
# Initialize time
t0 = datetime.datetime.now()  
# Set up Hamiltonian
for i in range(1, Ldim):  
    for j in range(1, Ldim):
        if abs(j - i) > 10:
            ham[j, i] = 0.0
        else:
            ham[j, i] = pow(0.3, abs(j - i))
    ham[i, i] = i
    coef[i] = 0.0
coef[1] = 1.0
err = 1.0
iter = 0
print("iter  ener      err ")
# Compute current E & normalize
while iter < 15 and err > 1.0e-6:  
    iter = iter + 1
    ener = 0.0
    ovlp = 0.0
    for i in range(1, Ldim):
        ovlp = ovlp + coef[i] * coef[i]
        sigma[i] = 0.0
        for j in range(1, Ldim):
            sigma[i] = sigma[i] + coef[j] * ham[j][i]
        ener = ener + coef[i] * sigma[i]
    ener = ener / ovlp
    for i in range(1, Ldim):
        coef[i] = coef[i] / sqrt(ovlp)
        sigma[i] = sigma[i] / sqrt(ovlp)
    err = 0.0
# Update
    for i in range(2, Ldim):  
        step = (sigma[i] - ener * coef[i]) / (ener - ham[i, i])
        coef[i] = coef[i] + step
        err = err + step * step
    err = sqrt(err)
    print((" %2d  %9.7f  %9.7f " % (iter, ener, err)))
# Elapsed time
delta_t = datetime.datetime.now() - t0  
print((" time = ", delta_t))
