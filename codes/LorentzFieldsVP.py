""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# LorentzFields.py:  Lorentz TF of E, B & V wi Visual

from vpython import *

scene = canvas(width=700, height=400, range=100, title="In O, Pure Bz(Dots)")
graf = curve(color=color.red)
rr = vector(40, 35, 0)
charge = sphere(canvas=scene, pos=rr, color=color.red, radius=2, make_trail=True)
scene2 = canvas(y=400, width=700, height=400, range=200, title="In O', Bz'(Dots) & Ex'")
charge2 = sphere(canvas=scene2, pos=rr, color=color.red, radius=2, make_trail=True)

B = vector(0, 0, 0.1)
# 3-D B in O, Bz
Bz = B.z
m0 = 1
# Mass, charge
q = 1
beta = 0.9
# v/c, Time step in O
dt = 0.001
gamma = 1 / sqrt(1.0 - beta**2)


# Plot B as dots
def plotB():
    for i in range(-100, 110, 10):
        for j in range(-50, 60, 10):
            points(pos=vector(i, j, 0), size=vector(2, 2, 2), canvas=scene, opacity=0.1)


# Plot B'  as dots
def plotBp():
    for i in range(-500, 501, 8):
        for j in range(-50, 60, 8):
            points(
                pos=vector(i, j, 0), size=vector(1, 1, 1), canvas=scene2, opacity=0.1
            )


# Euler method, solve Eq Mtn in O'
def Euler():
    V = vector(0.9, 0, 0)
    Vx = V.x
    # Vo in O
    Vy = V.y
    # Relative v
    v = vector(beta, 0, 0)
    # R(t=0)
    r = vector(40, 35, 0)
    den = 1 - Vx * beta
    Vxp = (V.x - beta) / den
    Vyp = Vy / den / gamma
    Vp = vector(Vxp, Vyp, 0)
    # Initial positions aligned
    rp = r
    # Motion loop
    for i in range(0, 200_000):
        rate(10_000)
        Bzp = gamma * Bz
        # B'
        Bp = vector(0, 0, Bzp)
        Eyp = -gamma * beta * Bz
        # E'
        Ep = vector(0, Eyp, 0)
        # Force
        F = V.cross(B)
        # Acceleration
        a = F / m0
        V = V + a * dt
        r = r + V * dt
        # Force in O'
        Fp = Vp.cross(Bp) + q * Ep
        # Mass in S'
        m = m0 * gamma
        # Acceleration in O'
        ap = Fp / m
        dtp = dt * gamma
        # V'
        Vp = Vp + ap * dtp
        # R'
        rp = rp + Vp * dtp - v * dtp
        # O' plot
        charge2.pos = vector(rp)
        # O plot
        charge.pos = vector(r)


plotB()
# Call plots
plotBp()
# Begin animation
Euler()

# Grace end of program
while True:
    rate(60)
