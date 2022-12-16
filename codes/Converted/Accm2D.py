""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2011; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2011.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# Accmd.Py: Python accelerated motion in 2D

from visual.graph import *


class Um1D:
# class constructor
    def __init__(self, x0, dt, vx0, ttot):  
# initial x position
        self.x00 = 0  
# time increment
        self.delt = dt  
# x velocity
        self.vx = vx0  
# total time
        self.time = ttot  
# total number steps
        self.steps = int(ttot / self.delt)  

# x position at time tt
    def x(self, tt):  
        return self.x00 + tt * self.vx

    """to be used in graphics"""

    def scenario(self, mxx, myy, mytitle, myxtitle, myytitle, xma, xmi, yma, ymi):
        graph = graph( x=mxx, y=myy, width=500, height=200, title=mytitle, xtitle=myxtitle, ytitle=myytitle, xmax=xma, xmin=xmi, ymax=yma, ymin=ymi, foreground=color.black, background=color.white, )

# produce file, plot 1D x motion
    def archive(self):  
        unimotion1D = gcurve(color=color.blue)
        tt = 0.0
# Disk file produced for 1D motion
        f = open("unimot1D.dat", "w")  
        for i in range(self.steps):
            xx = self.x(tt)
# Plots x vs time
            unimotion1D.plot(pos=(tt, xx))  
# x vs t for file
            f.write(" %f   %f\n" % (tt, xx))  
# increase time
            tt += self.delt  
# close disk file
        f.closed  


"""Uniform motion in 2D"""


# Um2D subclass of Um1D
class Um2D(Um1D):  
# Constructor Um2D
    def __init__(self, x0, dt, vx0, ttot, y0, vy0):  
# to construct Um1D
        Um1D.__init__(self, x0, dt, vx0, ttot)  
# initializes y position
        self.y00 = y0  
# initializes y velocity
        self.vy = vy0  

# produces y at time tt
    def y(self, tt):  
        return self.y00 + tt * self.vy

# overrides archive for 1D
    def archive(self):  
        unimot2d = gcurve(color=color.magenta)
        tt = 0.0
# Opens new Um2D file
        f = open("Um2D.dat", "w")  
        for i in range(self.steps):
            xx = self.x(tt)
            yy = self.y(tt)
# plots y vs x position
            unimot2d.plot(pos=(xx, yy))  
# writes x y in archive
            f.write(" %f   %f\n" % (xx, yy))  
            tt += self.delt
# closes open Um2D file
        f.closed  


"""Accelerated motion in 2D"""


# Daugther of U21D
class Accm2D(Um2D):  
    def __init__(self, x0, dt, vx0, ttot, y0, vy0, accx, accy):
# Um2D constructor
        Um2D.__init__(self, x0, dt, vx0, ttot, y0, vy0)  
# adds acceleretions
        self.ax = accx  
# to this class
        self.ay = accy  

    def xy(self, tt, i):
        self.xxac = self.x(tt) + self.ax * tt**2
        self.yyac = self.y(tt) + self.ay * tt**2
# if acceleration in x
        if i == 1:  
            return self.xxac
        else:
# if acceletation in y
            return self.yyac  

    def archive(self):
        acmotion = gcurve(color=color.red)
        tt = 0.0
        f = open("Accm2D.dat", "w")
        for i in range(self.steps):
            self.xxac = self.xy(tt, 1)
            self.yyac = self.xy(tt, 2)
# to disk file
            f.write(" %f   %f\n" % (self.xxac, self.yyac))  
# plot acc. motion
            acmotion.plot(pos=(self.xxac, self.yyac))  
            tt = tt + self.delt
        f.closed


# comment unmd um2d or myAcc to change plot
# x0, dt, vx0, ttot
unmd = Um1D(0.0, 0.1, 2.0, 4.0)  
# for 1D uniform motion
# For tmax tmin xmax xmin
unmd.scenario( 0, 0, "Uniform motion in  1D ",  "time", "x", 4.0, 0, 10.0, 0, )  
# archive 1D
unmd.archive()  
# x0, dt, vx0, ttot, y0, vy0
um2d = Um2D(0.0, 0.1, 2.0, 4.0, 0.0, 5.0)  
# for 2D uniform motion
# xmx xmin  ymax ymin
um2d.scenario( 0, 200, "Uniform motion in  2D ",  "x", "y", 10.0, 0, 25.0, 0, )  
# archive in two dim. motion
um2d.archive()  
myAcc = Accm2D(0.0, 0.1, 14.0, 4.0, 0.0, 14.0, 0.0, -9.8)
myAcc.scenario(0, 400, "Accelerated motion ", "x", "y", 55, 0, 5, -100.0)
# archive in accelerated motion
myAcc.archive()  
