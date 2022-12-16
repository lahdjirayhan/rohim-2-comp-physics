""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# TwoFileds.py:  Motion 2 charges, 2 frames wi Field TF & Visual

from vpython import *

scene = canvas(width=700, height=300, range=1, title="Frame S with moving charges")
graf = curve(color=color.red)
# charge up
r1 = vector(-0.9, 0.2, 0)  
charge = sphere(pos=r1, color=color.red, radius=0.02, make_trail=True)
# charge down
r2 = vector(-0.9, -0.2, 0)  
charge2 = sphere(pos=r2, color=color.red, radius=0.02, make_trail=True)
scene2 = canvas( y=300, width=700, height=300, range=1, title="Frame S' with velocity u to the right"
)
r1p = r1
r2p = r2
charge3 = sphere(color=color.red, radius=0.02, make_trail=True, canvas=scene2)
charge4 = sphere(color=color.red, radius=0.02, make_trail=True, canvas=scene2)
# permeability vacuum
mu0 = 1  
# in vacuum
e0 = 1  
# charge for  stronger interactions
q1 = 2  
q2 = 2
#  convenient for the units used
m0 = 50.0  
# time step in S
dt = 0.01  
# beta = v/c , v of S' wrt S
beta = 0.4  
gamma = 1 / sqrt(1 - beta**2)
m = m0 * gamma
# time increment in S' approx.1st time
dtp = dt * gamma  
# factor needed
facv = 1.0 / (1.0 - beta**2)  
# velocity os S' wrt to S
ux = beta  


# parameters: E, B in S
def EBtransform(E, B):  
# transformation of E and B to S'
    Exp = E.x  
    Eyp = gamma * (E.y - ux * B.z)
    Ezp = gamma * (E.z + ux * B.y)
    Bxp = B.x
    Byp = gamma * (B.y + ux * E.x)
    Bzp = gamma * (B.z - ux * E.y)
    Ep = vector(Exp, Eyp, Ezp)
    Bp = vector(Bxp, Byp, Bzp)
# returns E, B fiels in S?
    return Ep, Bp  


# Euler ODE solve
def EulerPlusTF(u, r1, r2, beta):  

# initial velocity of q1 in S
    u = vector(0.4, 0, 0)  
# initial position of q1 in S
    r1 = vector(-0.9, 0.2, 0)  
# initial position of q2 in S
    r2 = vector(-0.9, -0.2, 0)  
# each charge has the same velocity
    v2 = u  
# velocities of charges in S
    v1 = u  
    fcv1 = 1.0 / (1 - u.x * mag(v1))
# TF initial v's from S to S'
    v1xp = (v1.x - u.x) * fcv1  
    v1yp = v1.y * fcv1 / gamma
    v1zp = v1.z * fcv1 / gamma
    v1p = vector(v1xp, v1yp, v1zp)
    v2p = v1p
# initial positions coincide
    r1p = r1  
    r2p = r2

# loop for  motion
    for i in range(0, 300):  
# slow the motion
        rate(100)  
# position of q2 wrt r1
        rr1 = r2 - r1  
# position of q1 wrt r2
        rr2 = -rr1  
# magnitude of  rr1
        rr = mag(rr1)  
# B field at q2
        B1 = q1 * cross(v1, rr1) / (4 * pi * rr**3)  
# B field at q1
        B2 = q2 * cross(v2, rr2) / (4 * pi * rr**3)  
# E of q1 at q2
        E1 = q1 * rr1 / (4 * pi * rr**3)  
# E of q2 at q1
        E2 = q2 * rr2 / (4 * pi * rr**3)  
        E1p, B1p = EBtransform(E1, B1)
        E2p, B2p = EBtransform(E2, B2)
        ux = u.x
# magnetic force on q2
        FB1 = cross(v2, B1)  
# magnetic force on q1
        FB2 = cross(v1, B2)  
# Lorentz force on q1
        F2 = q1 * (E2 + FB2)  
# Lorentz force on q2
        F1 = q2 * (E1 + FB1)  
# magnetic force on q2
        FB1p = cross(v2p, B1p)  
# magnetic force on q2
        FB2p = cross(v1p, B2p)  
# Lorentz force on q2 in S'
        F1p = q2 * (E1p + FB1p)  
# Lorentz force on q1   in S'
        F2p = q1 * (E2p + FB2p)  
# acceleration q2 in S
        a2 = F1 / m0  
# acceleration q1 in S
        a1 = F2 / m0  
# acceleration q2 in S'
        a2p = F1p / m  
# acceleration q1 in S'
        a1p = F2p / m  
# velocity q1 in S
        v2 = v2 + a1 * dt  
# velocity q2 in S
        v1 = v1 + a2 * dt  
# x component of r (x1)
        x1 = r1.x  
        r1 = r1 + v2 * dt
# x component of r (x2) alfter dt
        x2 = r1.x  
        dx = x2 - x1
# time increment in S'
        dtp = (dt - dx * u.x) * gamma  
        r2 = r2 + v1 * dt
# velocity in S'
        v1p = v1p + a2p * dtp  
# velocity in S'
        v2p = v2p + a1p * dtp  
        r1p = r1p + v2p * dtp
        r2p = r2p + v1p * dtp
        charge3.pos = r1p
        charge4.pos = r2p
        charge2.pos = r2
        charge.pos = r1


# call to begin animation
EulerPlusTF()  
