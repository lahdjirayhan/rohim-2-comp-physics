""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# ImagePlaneViz.py: E field lines for charge plus image wi Visual

from visual.graph import *

scene = canvas( width=500, height=500, range=100, title="E of Charge Left of Plane (Red Image)"
)
plane = box( pos=vector(0, 0, 0), length=2, height=130, width=130, color=vector(0.9, 0.9, 0.9), opacity=0.5 )
gridpts = points(size=4, color=color.cyan)
PlusCharge = sphere(radius=5, color=color.red, pos=vector(40, 0, 0))
NegCharge = sphere(radius=5, color=color.green, pos=vector(-40, 0, 0))


def grid3d():
    for z in range(-60, 80, 20):
        for y in range(-60, 80, 20):
            for x in range(-60, 80, 20):
                gridpts.append(pos=vector(x, y, z))


def electricF():
    for y in range(-60, 80, 20):
        for z in range(-60, 80, 20):
            for x in range(-60, 80, 20):
# E vector here
                r = vector(x, y, z)  
# q location
                xx = vector(40, 0, 0)  
# Vector q to r
                d = vector(r - xx)  
# Vector q' to r
                dm = vector(r + xx)  
# Mag vector d
                dd = mag(d)  
# Mag vector dm
                ddp = mag(dm)  
                if xx.mag != 0:
# E due to q
                    E1 = d / dd**3  
# E due to -q
                    E2 = -dm / ddp**3  
# Total E
                    E = E1 + E2  
                    elecF = arrow(pos=r, color=color.orange)
# 10 x unit vector
                    elecF.axis = 10 * E / mag(E)  


grid3d()
electricF()
