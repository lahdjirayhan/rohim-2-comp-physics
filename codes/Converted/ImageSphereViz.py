""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# ImageSphereViz.py: E field lines for charge plus image wi Visual

from visual.graph import *

scene = canvas( width=500, height=500, range=100, title="E of Charge in Sphere (Red Image)"
)
gridpts = points(size=4, color=color.cyan)


def grid3d():
    for z in range(-60, 80, 20):
        for y in range(-60, 80, 20):
            for x in range(-60, 80, 20):
                gridpts.append(pos=vector(x, y, z))


grid3d()
xp = 60
yp = 40
zp = 0
a = 30
q = 1
# Charge location
xx = vector(xp, yp, zp)  
# Image location
xxp = xx * a**2 / (mag(xx)) ** 2  
# Image charge
qp = -q * a / mag(xx)  
ball = sphere(pos=vector(0, 0, 0), radius=a, opacity=0.5)
poscharge = sphere(radius=5, color=color.red, pos=vector(xp, yp, zp))
negcharge = sphere(radius=5, color=color.blue, pos=xxp)


def electricF():
    for y in range(-60, 80, 20):
        for z in range(-60, 80, 20):
            for x in range(-60, 80, 20):
# E here
                r = vector(x, y, z)  
# Vector q to r
                d = vector(r - xx)  
                dm = vector(r - xxp)
# Magnitude d
                dd = mag(d)  
# Magnitude dm
                ddp = mag(dm)  
                if xx.mag != 0:
# E due to q
                    E1 = d / dd**3  
# E due to -q
                    E2 = -dm / ddp**3  
                    E = E1 + E2
# E
                    elecF = arrow(pos=r, color=color.orange)  
# 10 x unit vector
                    elecF.axis = 10 * E / mag(E)  


electricF()
