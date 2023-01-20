""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# TwoCharges.py:  Motion of 2 charges in 2 frames wi Visual

from vpython import *

scene = canvas(
    width=700,
    height=300,
    range=1,
    background=vector(1, 1, 1),
    title="Frame O: Charges with Parallel Initial Velocities",
)
graf = curve(color=color.red)
r1 = vector(-0.9, 0.2, 0)
charge = sphere(pos=r1, color=color.red, radius=0.02, make_trail=True)
r2 = vector(-0.9, -0.2, 0)
charge2 = sphere(pos=r2, color=color.red, radius=0.02, make_trail=True)
scene2 = canvas(
    y=700,
    width=700,
    height=300,
    range=1,
    background=vector(1, 1, 1),
    title="Frame O':  Motion as Seen in Moving Frame",
)
r1p = r1
r2p = r2
charge3 = sphere(color=color.red, radius=0.02, make_trail=True, canvas=scene2)
charge4 = sphere(color=color.red, radius=0.02, make_trail=True, canvas=scene2)
mu0 = 1
e0 = 1
q1 = q2 = 2
m0 = 50.0
beta = 0.3
gamma = 1 / sqrt(1 - beta**2)
m = m0 * gamma
# Vo in O of q1
u = vector(0.3, 0, 0)
dt = 0.01
# Time step in O, O'
dtp = dt * gamma
r1 = vector(-0.9, 0.2, 0)
# Initial 1, 2
r2 = vector(-0.9, -0.2, 0)


# Euler ODE solve + Lorentz TF
def EulerPlusTF(u, r1, r2, beta):
    v2 = u
    v1 = u
    # Motion loop
    for i in range(0, 500):
        rate(100)
        # q2 wrt r1
        rr1 = r2 - r1
        # q1 wrt r2
        rr2 = -rr1
        rr = mag(rr1)
        # B at q2
        B1 = q1 * cross(v1, rr1) / (4 * pi * rr**3)
        # B at q1
        B2 = q2 * cross(v2, rr2) / (4 * pi * rr**3)
        # E at q2
        E1 = q1 * rr1 / (4 * pi * rr**3)
        # E at q1
        E2 = q2 * rr2 / (4 * pi * rr**3)
        # Force on q2
        F1 = q2 * (E1 + cross(v2, B1))
        # Force on q1
        F2 = q1 * (E2 + cross(v1, B2))
        a2 = F1 / m0
        a1 = F2 / m0
        v1 = v1 + a2 * dt
        v2 = v2 + a1 * dt
        x1 = r1.x
        r1 = r1 + v2 * dt
        # Update
        r2 = r2 + v1 * dt
        x1 = r1.x
        x2 = r2.x
        y1 = r1.y
        y2 = r2.y
        # Time in O
        t = i * dt
        #      Now transform to O'
        # TF x to x'
        x1p = (x1 - beta * t) / (sqrt(1 - beta * beta))
        # TF y to y'
        y1p = y1
        charge3.pos = vector(x1p, y1p, 0)
        x2p = (x2 - beta * t) / (sqrt(1 - beta * beta))
        y2p = y2
        charge3.pos = vector(x1p, y1p, 0)
        charge4.pos = vector(x2p, y2p, 0)
        charge2.pos = r2
        charge.pos = r1


# Call animation
EulerPlusTF(u, r1, r2, beta)
