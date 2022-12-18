""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# FDTD.py  FDTD Maxwell's equations in 1-D wi Visual

from vpython import *
import numpy as np

Xm = 201
Ym = 100
Zm = 100
ts = 2
beta = 0.01
Ex = np.zeros((Xm, ts), float)
# Arrays
Hy = np.zeros((Xm, ts), float)
#            Set up 3-D Plots
scene = canvas(
    x=0,
    y=0,
    width=800,
    height=500,
    title="E: blue, H: red. Periodic BC",
    forward=vector(-0.6, -0.5, -1),
    background=color.white,
)
Eplot = curve(
    pos=[(x, 0, 0) for x in range(Xm)],
    color=color.blue,
    radius=1.5,
)
Hplot = curve(
    pos=[(x, 0, 0) for x in range(Xm)],
    color=color.red,
    radius=1.5,
)
vplane = curve(
    pos=[(-Xm, Ym, 0), (Xm, Ym, 0), (Xm, -Ym, 0), (-Xm, -Ym, 0), (-Xm, Ym, 0)],
    color=color.cyan,
)
zaxis = curve(pos=[(-Xm, 0, 0), (Xm, 0, 0)], color=color.magenta)
hplane = curve(
    pos=[(-Xm, 0, Zm), (Xm, 0, Zm), (Xm, 0, -Zm), (-Xm, 0, -Zm), (-Xm, 0, Zm)],
    color=color.magenta,
)
ball1 = sphere(pos=vector(Xm + 30, 0, 0), color=color.black, radius=2)
ExLabel1 = label(text="Ex", pos=vector(-Xm - 10, 50, 0), box=0)
ExLabel2 = label(text="Ex", pos=vector(Xm + 10, 50, 0), box=0)
HyLabel = label(text="Hy", pos=vector(-Xm - 10, 0, 50), box=0)
zLabel = label(text="Z", pos=vector(Xm + 10, 0, 0), box=0)


def PlotFields():
    z = arange(Xm)
    # World to screen coords
    Eplot_x = 2 * z - Xm
    Eplot_y = 800 * Ex[z, 0]

    Hplot_x = 2 * z - Xm
    Hplot_z = 800 * Hy[z, 0]

    for i in range(Xm):
        Eplot.modify(i, x=Eplot_x[i], y=Eplot_y[i])
        Hplot.modify(i, x=Hplot_x[i], z=Hplot_z[i])


z = arange(Xm)
# Initial field
Ex[:Xm, 0] = 0.1 * np.sin(2 * pi * z / 100.0)
Hy[:Xm, 0] = 0.1 * np.sin(2 * pi * z / 100.0)
PlotFields()

while True:
    rate(30)
    Ex[1 : Xm - 1, 1] = Ex[1 : Xm - 1, 0] + beta * (Hy[0 : Xm - 2, 0] - Hy[2:Xm, 0])
    Hy[1 : Xm - 1, 1] = Hy[1 : Xm - 1, 0] + beta * (Ex[0 : Xm - 2, 0] - Ex[2:Xm, 0])
    # BC
    Ex[0, 1] = Ex[0, 0] + beta * (Hy[Xm - 2, 0] - Hy[1, 0])
    Ex[Xm - 1, 1] = Ex[Xm - 1, 0] + beta * (Hy[Xm - 2, 0] - Hy[1, 0])
    # BC
    Hy[0, 1] = Hy[0, 0] + beta * (Ex[Xm - 2, 0] - Ex[1, 0])
    Hy[Xm - 1, 1] = Hy[Xm - 1, 0] + beta * (Ex[Xm - 2, 0] - Ex[1, 0])
    PlotFields()
    # New -> old
    Ex[:Xm, 0] = Ex[:Xm, 1]
    Hy[:Xm, 0] = Hy[:Xm, 1]
