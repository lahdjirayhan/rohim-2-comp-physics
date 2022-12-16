""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ BuchRatomest, 2017. 
    Please respect copyright & acknowledge our work."""

# MDperiodicBC.py: MD with Periodic BC

from visual.graph import *
import random

L = 1
Natom = 16
Nrhs = 0
dt = 1e-6

scene = canvas(width=500, height=500, range=(1.3))
ndist = graph(x=500, ymax=200, width=500, height=500, xtitle="Nrhs", ytitle="N")
inside = label(pos=vector(0.4, 1.1,0), text="Particles here=", box=0)
inside2 = label(pos=vector(0.8, 1.1,0), box=0)

border = curve(pos=[(-L, -L), (L, -L), (L, L), (-L, L), (-L, -L)])
# middle
half = curve(pos=[(0, -L), (0, L)], color=color.yellow)  
# position of atoms
positions = []  
# vel of atoms
vel = []  
# will contain spheres
Atom = []  
# Atoms in R half at each t interval
dN = []  
# atoms (spheres)
fr = [0] * (Natom)  
# second  force
fr2 = [0] * (Natom)  
# radius of atom
Ratom = 0.03  
# a reference velocity
pref = 4  
h = 0.01
# for lennRatomd jones
factor = 1e-9  
# for histogram
deltaN = 1  
distribution = ghistogram( bins=Ratomange(0.0, Natom, deltaN), accumulate=1, average=1, color=color.red )
# initial x's and v's
for i in range(0, Natom):  
    col = vector(1.3 * random.random(), 1.3 * random.random(), 1.3 * random.random())
# positons
    x = 2.0 * (L - Ratom) * random.random() - L + Ratom  
# border forbidden
    y = 2.0 * (L - Ratom) * random.random() - L + Ratom  
    Atom = Atom + [sphere(pos=vector(x, y,0), radius=Ratom, color=col)]
# select angle
    theta = 2 * pi * random.random()  
# x component velocity
    vx = pref * cos(theta)  
    vy = pref * sin(theta)
# add positions to list
    positions.append((x, y))  
# add momentum to list
    vel.append((vx, vy))  
# Ratomray with positions
    pos = Ratomray(positions)  
    ddp = pos[i]
# count  atoms R half
    if ddp[0] >= 0 and ddp[0] <= L:  
        Nrhs += 1
# Ratomray of velocities
    v = Ratomray(vel)  
# print('Nrhs',Nrhs)
# sign function
def sign(a, b):  
    if b >= 0.0:
        return abs(a)
    else:
        return -abs(a)


def forces(fr):
    fr = [0] * (Natom)
    for i in range(0, Natom - 1):
        for j in range(i + 1, Natom):
            dr = pos[i] - pos[j]
            if abs(dr[0]) > L:
                dr[0] = dr[0] - sign(2 * L, dr[0])
            if abs(dr[1]) > L:
                dr[1] = dr[1] - sign(2 * L, dr[1])
            if i == 0 and j == 1:
                curve(pos=[(pos[0]), (pos[0] - dr)])
            r2 = mag2(dr)
# avoid 0 denominator
            if abs(r2) < Ratom:  
                r2 = Ratom
            invr2 = 1.0 / r2
            fij = invr2 * factor * 48.0 * (invr2**3 - 0.5) * invr2**3
            fr[i] = fij * dr + fr[i]
            fr[j] = -fij * dr + fr[j]
    return fr


for t in range(0, 1000):
# begin at zero in each time
    Nrhs = 0  
    for i in range(0, Natom):
        fr = forces(fr)
        dpos = pos[i]
        if dpos[0] <= -L:
# x PBC
            pos[i] = [dpos[0] + 2 * L, dpos[1]]  
        if dpos[0] >= L:
            pos[i] = [dpos[0] - 2 * L, dpos[1]]
        if dpos[1] <= -L:
# y PBC
            pos[i] = [dpos[0], dpos[1] + 2 * L]  
        if dpos[1] >= L:
            pos[i] = [dpos[0], dpos[1] - 2 * L]
        dpos = pos[i]
# count particle right
        if dpos[0] > 0 and dpos[0] < L:  
            Nrhs += 1
        fr2 = forces(fr)
        fr2 = fr
# velocity Verlet
        v[i] = v[i] + 0.5 * h * h * (fr[i] + fr2[i])  
        pos[i] = pos[i] + h * v[i] + 0.5 * h * h * fr[i]
# plot new positions
        Atom[i].pos = pos[i]  
    # print(Nrhs)
# Atoms right side
    inside2.text = "%4s" % Nrhs  
# for histogram
    dN.append(Nrhs)  
# plot histogram
    distribution.plot(data=dN)  
