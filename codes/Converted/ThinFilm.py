""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# ThinFilm.py: Thin film interference by reflection (AJP 72,1248-1253)

from visual.graph import *

escene = canvas( width=500, height=500, range=400, background=color.white, foreground=color.black, title="Thin Film Interference", )
# Red intensities
Rcurve = curve(color=color.red)  
# Green intensities
Gcurve = curve(color=color.green)  
# Blue intensities
Bcurve = curve(color=color.blue)  
title = label(pos=vector(-20, 350, 0), text="Intensity vs Thickness nA in nm", box=0)
waves = label(pos=vector(-30, 320, 0), text="Red, Green, and Blue Intensities", box=0)
trans = label(pos=vector(-280, 300, 0), text="Transmission", box=0)
refl = label(pos=vector(210, 300, 0), text="Reflection", box=0)
lamR = 572
lamB = 430
lamG = 540
# R,B, G wavelengths
i = 0  
film = curve(pos=[(-150, -250), (150, -250), (150, 250), (-150, 250), (-150, -250)])
Rc = []
Gc = []
# R,G,B intensity arrays
Bc = []  
nA = arange(0, 1250, 10)
delR = 2 * pi * nA / lamR + pi
delG = 2 * pi * nA / lamG + pi
delB = 2 * pi * nA / lamB + pi
intR = (cos(delR / 2)) ** 2
intG = (cos(delG / 2)) ** 2
intB = (cos(delB / 2)) ** 2
xrp = 300 * intR - 150
xbp = 300 * intB - 150
# Linear TFs
xgp = 300 * intG - 150  
# Film height
ap = -500 * nA / 1240 + 250  
Rcurve.x = xrp
Rcurve.y = ap
Gcurve.x = xgp
Gcurve.y = ap
Bcurve.x = xbp
Bcurve.y = ap
Rc = Rc + [intR]
Gc = Gc + [intG]
# Fill I's
Bc = Bc + [intB]  
Rt = []
Gt = []
Bt = []
DelRt = 4 * pi * nA / lamR
DelGt = 4 * pi * nA / lamG
DelBt = 4 * pi * nA / lamB
IntRt = cos(DelRt / 2) ** 2
IntGt = cos(DelGt / 2) ** 2
IntBt = cos(DelBt / 2) ** 2
xRpt = 300 * intR - 150
xBpt = 300 * intB - 150
xGpt = 300 * intG - 150
Rt = Rt + [intR]
Gt = Gt + [intG]
Bt = Bt + [intB]
#  Film height
ap = -500 * nA / 1240 + 250  

for nA in range(0, 125):
# RGB reflection
    col = vector(intR[nA], intG[nA], intB[nA])  
    reflesc = -500 * nA / 125 + 250
    box(pos=vector(205, reflesc, 0), width=0.1, height=10, length=50, color=col)
# Colors by transmission
    colt = vector(IntRt[nA], IntGt[nA], IntBt[nA])  
    box(pos=vector(-270, reflesc, 0), width=0.1, height=10, length=50, color=colt)
# Labels for vertical axis
    if nA % 20 == 0:  
        prof = nA * 10
        escal = -500 * nA / 125 + 250
        print(escal)
        depth = label(pos=vector(-200, escal, 0), text="%4d" % prof, box=0)
