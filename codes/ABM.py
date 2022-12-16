""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# ABM.py:   Adams BM method to integrate ODE
# Solves y' = (t - y)/2,    with y[0] = 1 over [0, 3]

from vpython import *

numgr = graph( x=0, y=0, width=600, height=300, xmin=0.0, xmax=3.0, title="Numerical Solution", xtitle="t", ytitle="y", ymax=2.0, ymin=0.9, )
numsol = gcurve(color=color.yellow, canvas=numgr)
exactgr = graph( x=0, y=300, width=600, height=300, title="Exact solution", xtitle="t", ytitle="y", xmax=3.0, xmin=0.0, ymax=2.0, ymin=0.9, )

exsol = gcurve(color=color.cyan, canvas=exactgr)
# N steps > 3
n = 24  
A = 0
B = 3.0
t = [0] * 500
y = [0] * 500
yy = [0] * 4


# RHS F function
def f(t, y):  
    return (t - y) / 2.0


def rk4(t, yy, h1):
    for i in range(0, 3):
        t = h1 * i
        k0 = h1 * f(t, y[i])
        k1 = h1 * f(t + h1 / 2.0, yy[i] + k0 / 2.0)
        k2 = h1 * f(t + h1 / 2.0, yy[i] + k1 / 2.0)
        k3 = h1 * f(t + h1, yy[i] + k2)
        yy[i + 1] = yy[i] + (1.0 / 6.0) * (k0 + 2.0 * k1 + 2.0 * k2 + k3)
        print((i, yy[i]))
    return yy[3]


def ABM(a, b, N):
    # Compute 3 additional starting values using rk
# step
    h = (b - a) / N  
    t[0] = a
    y[0] = 1.00
    F0 = f(t[0], y[0])
    for k in range(1, 4):
        t[k] = a + k * h
# 1st step
    y[1] = rk4(t[1], y, h)  
# 2nd step
    y[2] = rk4(t[2], y, h)  
# 3rd step
    y[3] = rk4(t[3], y, h)  
    F1 = f(t[1], y[1])
    F2 = f(t[2], y[2])
    F3 = f(t[3], y[3])
    h2 = h / 24.0

# Predictor
    for k in range(3, N):  
        p = y[k] + h2 * (-9.0 * F0 + 37.0 * F1 - 59.0 * F2 + 55.0 * F3)
# Next abscissa
        t[k + 1] = a + h * (k + 1)  
        F4 = f(t[k + 1], p)
# Corrector
        y[k + 1] = y[k] + h2 * (F1 - 5.0 * F2 + 19.0 * F3 + 9.0 * F4)  
# Update values
        F0 = F1  
        F1 = F2
        F2 = F3
        F3 = f(t[k + 1], y[k + 1])
    return t, y


print("  k     t      Y numerical      Y exact")
t, y = ABM(A, B, n)
for k in range(0, n + 1):
    print( ( " %3d  %5.3f  %12.11f  %12.11f "
            % (k, t[k], y[k], (3.0 * exp(-t[k] / 2.0) - 2.0 + t[k]))
        )
    )
    numsol.plot(pos=(t[k], y[k]))
    exsol.plot(pos=(t[k], 3.0 * exp(-t[k] / 2.0) - 2.0 + t[k]))
