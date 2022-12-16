""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# MDsplitBox.py: Counting particle in split box

from vpython import *
import random

L = 1
deltaN = 1
Natoms = 16
dt = 1e-6
ar = 0.03
t = 1
twoN = 2**Natoms
Nrhs = 0
prob = [0] * (Natoms)
dN = [0] * (Natoms)
Atom = []

scene = canvas(width=400, height=400, range=(1.3))
ndist = graph( x=400, ymax=100, width=400, height=400, xtitle="Nrhs", ytitle="N", title="Numb Times Nrhs Particles Occur", )
distribution = ghistogram( bins=arange(1.0, Natoms, deltaN), accumulate=1, average=1, color=color.red )
scene2 = graph( y=400, height=400, width=400, xmin=0, xmax=16, ymin=0, ymax=0.01, title="Probability of Nrhs", ytitle="P(n)/2**N", xtitle="Nrhs", )
dis = gvbars(delta=0.5, color=color.red, canvas=scene2)

while t < 1000:
    positions = []
    curve(pos=[(-L, -L), (L, -L), (L, L), (-L, L), (-L, -L)])
    curve(pos=[(0, -L), (0, L)], color=color.yellow)
    inside = label(pos=vector(0.2, 1.1,0), text="Numb RHS Particles =", box=0)
    inside2 = label(pos=vector(0.8, 1.1,0), box=0)
# Initial x & v
    for i in range(Natoms):  
        rate(10)
# Atom locations
        x = 2.0 * (L - ar) * random.random() - L + ar  
        y = 2.0 * (L - ar) * random.random() - L + ar
        Atom = Atom + [sphere(pos=vector(x, y,0), radius=ar, color=color.green)]
        positions.append((x, y))
        pos = array(positions)
        ddp = pos[i]
        if ddp[0] >= 0 and ddp[0] <= L:
# Count initial
            Nrhs += 1  
        inside2.text = "%4s" % Nrhs
# Histogram
    dN.append(Nrhs)  
# Plot histogram
    distribution.plot(data=dN)  
    prob[Nrhs] += 1
# Probabilities
    dis.plot(pos=(Nrhs, prob[Nrhs] / twoN))  
# Start new walk
    for obj in scene.objects:  
        if obj is curve or obj is sphere or obj is label:
            continue
        else:
# Clear curve
            obj.visible = 0  
    inside2.text = "%4s" % Nrhs
    Nrhs = 0
    t += 1
