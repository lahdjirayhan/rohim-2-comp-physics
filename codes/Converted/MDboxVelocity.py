from vpython import *
import random

# side square
L = 1  
# minimum value for velocity
minix = 2.0  
# max value for velocity
maxix = 6.0  
scene = canvas(width=500, height=500, range=(1.3))
ndist = graph( x=500, ymax=300, xmin=minix, xmax=maxix, width=500, height=500, xtitle="v", ytitle="Nv", )
inside = label(pos=vector(0.4, 1.1,0), text="Particles here=", box=0)
inside2 = label(pos=vector(0.8, 1.1,0), box=0)
# number of atoms
Natom = 16  
# number particles right side
Nr = 0  
# time step
dt = 1e-6  
# limits figure
border = curve(pos=[(-L, -L), (L, -L), (L, L), (-L, L), (-L, -L)])  
# middle
half = curve(pos=[(0, -L), (0, L)], color=color.yellow)  
# position of atoms
positions = []  
# vel of atoms
vel = []  
# will contain spheres
Atom = []  
# will contain atoms in right half at each tieme interval
dv = []  
# atoms (spheres)
fr = [0] * (Natom)  
# second  force
fr2 = [0] * (Natom)  
# radius of atom
ar = 0.03  
# a reference velocity
vini = 4.5  
h = 0.008
# for lennard jones
factor = 1e-11  
# for histogram
deltav = 0.13  

# initial positions and velocities
for i in range(0, Natom):  
    col = vector(1.3 * random.random(), 1.3 * random.random(), 1.3 * random.random())
# positons of atoms
    x = 2.0 * (L - ar) * random.random() - L + ar  
# in the border forbidden
    y = 2.0 * (L - ar) * random.random() - L + ar  
# add atoms
    Atom = Atom + [sphere(pos=vector(x, y,0), radius=ar, color=col)]  
# select angle  0<=theta<= 2pi
    theta = 2 * pi * random.random()  
# x component velocity
    vx = vini * cos(theta)  
    vy = vini * sin(theta)
# add positions to list
    positions.append((x, y))  
# add momentum to list
    vel.append((vx, vy))  
# array with positions
    pos = array(positions)  
    ddp = pos[i]
# count initial atoms at right half
    if ddp[0] >= 0 and ddp[0] <= L:  
        Nr += 1
# array of velocities
    v = array(vel)  

# print('Nr',Nr)
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
# relative position between particles
            dr = pos[i] - pos[j]  
# smallest distance from part.or image
            if abs(dr[0]) > L:  
# interact with closer image
                dr[0] = dr[0] - sign(2 * L, dr[0])  
# same for y
            if abs(dr[1]) > L:  
                dr[1] = dr[1] - sign(2 * L, dr[1])
# magnitude dr squared
            r2 = mag2(dr)  
            # print(r2)
# to avoid 0 denominator
            if r2 < 0.01:  
                # print('      ',r2)
# minimum distance between 2 atoms)**2
                r2 = 0.01  

# compute this factor
            invr2 = 1.0 / r2  
#
            fij = invr2 * factor * 48.0 * (invr2**3 - 0.5) * invr2**3  
            fr[i] = fij * dr + fr[i]
# lennard jones force
            fr[j] = -fij * dr + fr[j]  
    return fr


distribution = ghistogram( bins=arange(minix, maxix, deltav), accumulate=1, average=1, color=color.red )
# time steps
for t in range(0, 2000):  
# begin at zero in each time
    Nr = 0  
    if t % 100 == 0:
        print(("t ", t))
    for i in range(0, Natom):
        fr = forces(fr)
        dpos = pos[i]
        if dpos[0] <= -L:
# x periodic boundary conditions
            pos[i] = [dpos[0] + 2 * L, dpos[1]]  
        if dpos[0] >= L:
            pos[i] = [dpos[0] - 2 * L, dpos[1]]
        if dpos[1] <= -L:
# y periodic boundary conditions
            pos[i] = [dpos[0], dpos[1] + 2 * L]  
        if dpos[1] >= L:
            pos[i] = [dpos[0], dpos[1] - 2 * L]
        dpos = pos[i]
# count particles at right
        if dpos[0] > 0 and dpos[0] < L:  
            Nr += 1
        fr2 = forces(fr)
        fr2 = fr
# velocity Verlet algorithm
        v[i] = v[i] + 0.5 * h * h * (fr[i] + fr2[i])  
        pos[i] = pos[i] + h * v[i] + 0.5 * h * h * fr[i]
# plot atoms at new positions
        Atom[i].pos = pos[i]  
        dvel = mag(v[i])
# particles in right side
    inside2.text = "%4s" % Nr  
# for the histogram
    dv.append(dvel)  
# plot histogram
    distribution.plot(data=dv)  
