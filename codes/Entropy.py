""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Entropy.py Shannon Entropy with Logistic map using Tkinter

try:
    from tkinter import *
except:
    from tkinter import *
import math
from numpy import zeros, arange

global Xwidth, Yheight
root = Tk()
root.title("Entropy versus mu ")
mumin = 3.5
mumax = 4.0
dmu = 0.25
nbin = 1000
nmax = 100000
prob = zeros((1000), float)
minx = mumin
maxx = mumax
miny = 0
maxy = 2.5
Xwidth = 500
Yheight = 500

# initialize canvas
c = Canvas(root, width=Xwidth, height=Yheight)  
# pack canvas
c.pack()  

# to begin quit
Button(root, text="Quit", command=root.quit).pack()  


# x - left, y - top, x - right, y - bottom
def world2sc(xl, yt, xr, yb):  
# canvas width          _________________________
    maxx = Xwidth  
# canvas height         |      |    |tm         |
    maxy = Yheight  
# left margin           |   ___|____|_______ ___|
    lm = 0.10 * maxx  
# right margin          |lm |  |            |   |
    rm = 0.90 * maxx  
# bottom margin         |___|  |            |   |
    bm = 0.85 * maxy  
# top margin            |__ |__|____________|   |
    tm = 0.10 * maxy  
#              |   |  bm         rm|   |
    mx = (lm - rm) / (xl - xr)  
#        |   |__|____________|   |
    bx = (xl * rm - xr * lm) / (xl - xr)  
#        |                       |
    my = (tm - bm) / (yt - yb)  
#        |_______________________|
    by = (yb * tm - yt * bm) / (yb - yt)  
# (maxx, maxy)
    linearTr = [mx, bx, my, by]  
# returns a list with 4 elements
    return linearTr  


# Plot y, x, axes; world coord converted to canvas coordinates
# to be called after call workd2sc
def xyaxis(mx, bx, my, by):  
# minima and maxima converted to
    x1 = (int)(mx * minx + bx)  
# canvas coordinades
    x2 = (int)(mx * maxx + bx)  
    y1 = (int)(my * maxy + by)
    y2 = (int)(my * miny + by)
    yc = (int)(my * 0.0 + by)
# x axis
    c.create_line(x1, yc, x2, yc, fill="red")  
# y - axis
    c.create_line(x1, y1, x1, y2, fill="red")  
# x tics
    for i in range(7):  
# world coordinates
        x = minx + (i - 1) * 0.1  
# canvas coord
        x1 = (int)(mx * x + bx)  
        x2 = (int)(mx * minx + bx)
# real coordinates
        y = miny + i * 0.5  
# canvas coords
        y2 = (int)(my * y + by)  
# tics x
        c.create_line(x1, yc - 4, x1, yc + 4, fill="red")  
# tics y
        c.create_line(x2 - 4, y2, x2 + 4, y2, fill="red")  
# x axis
        c.create_text( x1 + 10, yc + 10, text="%5.2f" % (x), fill="red", anchor=E )  
# y axis
        c.create_text(x2 + 30, y2, text="%5.2f" % (y), fill="red", anchor=E)  
    c.create_text(70, 30, text="Entropy", fill="red", anchor=E)
    c.create_text(420, yc - 10, text="mu", fill="red", anchor=E)


# returns list
mx, bx, my, by = world2sc(minx, maxy, maxx, miny)  
# axes values
xyaxis(mx, bx, my, by)  
mu0 = mumin * mx + bx
entr0 = my * 0.0 + by
# mu loop
for mu in arange(mumin, mumax, dmu):  
    print(mu)
    for j in range(1, nbin):
        prob[j] = 0
    y = 0.5
    for n in range(1, nmax + 1):
# Logistic map, Skip transients
        y = mu * y * (1.0 - y)  
        if n > 30000:
            ibin = int(y * nbin) + 1
            prob[ibin] += 1
    entropy = 0.0
    for ibin in range(1, nbin):
        if prob[ibin] > 0:
            entropy = entropy - (prob[ibin] / nmax) * math.log10(prob[ibin] / nmax)
# entropy to canvas coords
    entrpc = my * entropy + by  
# mu to canvas coords
    muc = mx * mu + bx  
    c.create_line(mu0, entr0, muc, entrpc, width=1, fill="blue")
# begin values for next line
    mu0 = muc  
    entr0 = entrpc
# makes effective events
root.mainloop()  
