""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# DielectVis.py: Visual Animated FDTD E & B free space to dielectric

from visual import *

Xmax = 401
Ymax = 100
Zmax = 100
scene = canvas( x=0, y=0, width=800, height=500, title="Hy (cyan), \
        Ex (yellow),     Dielectric (gray)",
    forward=vector(0.0, -0.3, -0.7),
)
Hplot = curve(x=list(range(0, Xmax)), color=color.cyan, radius=1.5, canvas=scene)
Eplot = curve(x=list(range(0, Xmax)), color=color.yellow, radius=1.5, canvas=scene)
vplane = curve( pos=[(-Xmax, Ymax), (Xmax, Ymax), (Xmax, -Ymax), (-Xmax, -Ymax), (-Xmax, Ymax)], color=color.cyan, )
zaxis = curve(pos=[(-Xmax, 0), (Xmax, 0)], color=color.magenta)
hplane = curve( pos=[ (-Xmax, 0, Zmax), (Xmax, 0, Zmax), (Xmax, 0, -Zmax), (-Xmax, 0, -Zmax), (-Xmax, 0, Zmax), ], color=color.magenta, )
sep = box(width=180, height=200, length=400, pos=vector(200, 0, 0), opacity=0.5)
eps = 4
dd = 0.5
# Dielectric, Stability const
Xmax = 401  
Ex = zeros((Xmax), float)
# Declare fields, 2 t's
Hy = zeros((Xmax), float)  
beta = zeros((Xmax), float)
z = arange(201)
Ex[:201] = 0.5 * sin(2 * pi * z / 100)
# Init fields
Hy[:201] = 0.5 * sin(2 * pi * z / 100)  

for i in range(0, 401):
    if i < 201:
# Free space
        beta[i] = dd  
    else:
# Dielectric
        beta[i] = dd / eps  
Hylabel1 = label(text="Ex", pos=vector(-Xmax - 10, 120,0), box=0)
Exlabel = label(text="Hy", pos=vector(-Xmax - 10, 0, 50), box=0)
# Shifts fig
zlabel = label(text="Z", pos=vector(Xmax + 10, 0,0), box=0)  
polfield = arrow(canvas=scene)
polfield2 = arrow(canvas=scene)


def plotfields():
    k = arange(Xmax)
# World to screen coords
    Hplot.x = 2 * k - Xmax  
    Hplot.z = 150 * Hy[k]
    Eplot.x = 2 * k - Xmax
    Eplot.y = 150 * Ex[k]


plotfields()
# Time evolution
for i in range(0, 400):  
    rate(50)
# Field propagation
    for k in range(1, Xmax - 1):  
        Ex[k] = Ex[k] + beta[k] * (Hy[k - 1] - Hy[k])
        Hy[k] = Hy[k] + dd * (Ex[k] - Ex[k + 1])
    plotfields()
