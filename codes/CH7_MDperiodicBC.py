""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ BuchRatomest, 2017.
    Please respect copyright & acknowledge our work."""

# MDperiodicBC.py: MD with Periodic BC

from vpython import *
import random
import numpy as np

L = 1
Natom = 16
Nrhs = 0
dt = 1e-6
dN = np.zeros(16)

ndist = graph(
    ymax=200, width=400, height=300, xtitle="Particles in right half", ytitle="N"
)
bars = gvbars(delta=0.8, color=color.red)

scene = canvas(width=400, height=400, range=(1.3))
inside = label(pos=vector(0.4, 1.1, 0), text="Particles here=", box=0)
inside2 = label(pos=vector(0.8, 1.1, 0), box=0)
border = curve(pos=[(-L, -L, 0), (L, -L, 0), (L, L, 0), (-L, L, 0), (-L, -L, 0)])
# middle
half = curve(pos=[(0, -L, 0), (0, L, 0)], color=color.yellow)
# position of atoms
positions = []
# vel of atoms
vel = []
# will contain spheres
Atom = []
# atoms (spheres)
fr = [0] * (Natom)
# second  force
fr2 = [0] * (Natom)
# radius of atom
Ratom = 0.03
# a reference velocity
pref = 5
h = 0.01
# for lennRatomd jones
factor = 1e-9

for i in range(0, Natom):
    col = vector(1.3 * random.random(), 1.3 * random.random(), 1.3 * random.random())
    x = 2.0 * (L - Ratom) * random.random() - L + Ratom  # Positions
    y = 2.0 * (L - Ratom) * random.random() - L + Ratom  # Border forbidden

    Atom = Atom + [sphere(pos=vec(x, y, 0), radius=Ratom, color=col)]

    # Select angle
    theta = 2 * pi * random.random()

    # Component velocity
    vx = pref * cos(theta)
    vy = pref * sin(theta)

    # Add positions and momentum to list
    positions.append((x, y, 0))
    vel.append((vx, vy, 0))

    posi = np.array(positions)
    ddp = posi[i]

    if 0 < ddp[0] <= L:
        Nrhs += 1  # count atoms R half

    v = np.array(vel)  # Ratomray of velocities


def sign(a, b):
    if b >= 0.0:
        return abs(a)
    else:
        return -abs(a)


def forces(fr):
    fr = [0] * (Natom)
    for i in range(0, Natom - 1):
        for j in range(i + 1, Natom):
            dr = posi[i] - posi[j]
            if abs(dr[0] > L):
                dr[0] = dr[0] - sign(2 * L, dr[0])

            if abs(dr[1] > L):
                dr[1] = dr[1] - sign(2 * L, dr[1])

            r2 = dr[0] ** 2 + dr[1] ** 2 + dr[2] ** 2

            # Avoid 0 denominator
            if abs(r2) < Ratom:
                r2 = Ratom

            invr2 = 1.0 / r2

            fij = invr2 * factor * 48.0 * (invr2**3 - 0.5) * invr2**3
            fr[i] = fij * dr + fr[i]
            fr[j] = -fij * dr + fr[j]

    return fr


for t in range(100):
    print(t)
    Nrhs = 0

    for i in range(0, Natom):
        fr = forces(fr)
        dpos = posi[i]  # periodic BC

        if dpos[0] <= -L:
            posi[i] = (dpos[0] + 2 * L, dpos[1], 0)

        if dpos[0] >= L:
            posi[i] = (dpos[0] - 2 * L, dpos[1], 0)

        if dpos[1] <= -L:
            posi[i] = (dpos[0], dpos[1] + 2 * L, 0)

        if dpos[1] >= L:
            posi[i] = (dpos[0], dpos[1] - 2 * L, 0)

        # count particle right
        if 0 < dpos[0] < L:
            Nrhs += 1

        fr2 = forces(fr)

        # velocity Verlet
        v[i] = v[i] + 0.5 * h * h * (fr[i] + fr2[i])
        posi[i] = posi[i] + h * v[i] + 0.5 * h * h * fr[i]

        aa = posi[i]
        Atom[i].pos = vector(aa[0], aa[1], aa[2])

    dN[Nrhs] += 1
    inside2.text = "%4s" % Nrhs

    for j in arange(0, 16):
        bars.plot(pos=vec(j, dN[j], 0))

    rate(5)

print("finished")
