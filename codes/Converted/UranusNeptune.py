""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# UranusNeptune.py: Orbits of Neptune & Uranus

from visual.graph import *

scene = canvas(width=600, height=600, title="White Neptune & Black Uranus", range=40)
sun = sphere(pos=vector(0, 0, 0), radius=2, color=color.yellow)
escenau = graph( x=600, width=400, height=400, title="Pertubation of Uranus Angular Position"
)
graphu = gcurve(color=color.cyan)

escenan = graph(x=800, y=400, width=400, height=400)
graphn = gcurve(color=color.white)
rfactor = 1.8e-9
# in units T in years, R AU, Msun=1
G = 4 * pi * pi  
# mass Uranus in solar masses
mu = 4.366244e-5  
# mass Sun
M = 1.0  
# Neptune mass in solar masses
mn = 5.151389e-5  
# distance Uranus Sun in AU
du = 19.1914  
# distance Neptune sun in AU
dn = 30.0611  
# Uranus Orbital Period yr
Tur = 84.0110  
# Neptune Orbital Period yr
Tnp = 164.7901  
# Uranus angular velocity (2pi/T)
omeur = 2 * pi / Tur  
# Neptune angular velocity
omennp = 2 * pi / Tnp  
omreal = omeur
# Uranus orbital velocity UA/yr
urvel = 2 * pi * du / Tur  
# Neptune orbital velocity UA/yr
npvel = 2 * pi * dn / Tnp  
# 1 Uranus at lon 2 gr 16 min sep 1821
# to radians in 1690 -wrt x-axis
radur = (205.64) * pi / 180.0  
# init x- pos ur. in 1690
urx = du * cos(radur)  
# init y-pos ur in 1690
ury = du * sin(radur)  
urvelx = urvel * sin(radur)
urvely = -urvel * cos(radur)
# 1690 Neptune at long.
# 1690 rad neptune wrt x-axis
radnp = (288.38) * pi / 180.0  
uranus = sphere(pos=vector(urx, ury, 0), radius=0.5, color=vector(0.88, 1, 1), make_trail=True)
urpert = sphere(pos=vector(urx, ury, 0), radius=0.5, color=vector(0.88, 1, 1), make_trail=True)
fnu = arrow(pos=uranus.pos, color=color.orange, axis=vector(0, 4, 0))
# init coord x neptune 1690
npx = dn * cos(radnp)  
#           y
npy = dn * sin(radnp)  
npvelx = npvel * sin(radnp)
npvely = -npvel * cos(radnp)
neptune = sphere(pos=vector(npx, npy, 0), radius=0.4, color=color.cyan, make_trail=True)
fun = arrow(pos=neptune.pos, color=color.orange, axis=vector(0, -4, 0))
nppert = sphere(pos=vector(npx, npy, 0), radius=0.4, color=color.white, make_trail=True)
# initial vector velocity Uranus
velour = vector(urvelx, urvely, 0)  
# initial vector velocity Neptune
velnp = vector(npvelx, npvely, 0)  
# time increment in terrestrial year
dt = 0.5  
# initial position Uranus wrt Sun
r = vector(urx, ury, 0)  
# initial position Neptune wrt Sun
rnp = vector(npx, npy, 0)  
veltot = velour
veltotnp = velnp
rtot = r
rtotnp = rnp


# i==1 Uranus  i==2 Neptune
def ftotal(r, rnp, i):  
# Force sun over URANUS
    Fus = -G * M * mu * r / (du**3)  
# Force Sun over NEPTUNE
    Fns = -G * M * mn * rnp / (dn**3)  
# distance Neptune-Uranus
    dnu = mag(rnp - r)  
# force N on U
    Fnu = -G * mu * mn * (rnp - r) / (dnu**3)  
# force uranus on Neptune
    Fun = -Fnu  
# total force on U (sun + N)
    Ftotur = Fus + Fnu  
# On Neptune F sun +F urn
    Ftotnp = Fns + Fun  
    if i == 1:
        return Ftotur
    else:
        return Ftotnp


# on Neptune
def rkn(r, veltot, rnp, m, i):  
    k1v = ftotal(r, rnp, i) / m
    k1r = veltot
    k2v = ftotal(r, rnp + 0.5 * k1r * dt, i) / m
    k2r = veltot + 0.5 * k2v * dt
    k3v = ftotal(r, rnp + 0.5 * k2r * dt, i) / m
    k3r = veltot + 0.5 * k3v * dt
    k4v = ftotal(r, rnp + k3r * dt, i) / m
    k4r = veltot + k4v * dt
    veltot = veltot + (k1v + 2 * k2v + 2 * k3v + k4v) * dt / 6.0
    rnp = rnp + (k1r + 2 * k2r + 2 * k3r + k4r) * dt / 6.0
    return r, veltot


# on Uranus
def rk(r, veltot, rnp, m, i):  
    k1v = ftotal(r, rnp, i) / m
    k1r = veltot
    k2v = ftotal(r + 0.5 * k1r * dt, rnp, i) / m
    k2r = veltot + 0.5 * k2v * dt
    k3v = ftotal(r + 0.5 * k2r * dt, rnp, i) / m
    k3r = veltot + 0.5 * k3v * dt
    k4v = ftotal(r + k3r * dt, rnp, i) / m
    k4r = veltot + k4v * dt
    veltot = veltot + (k1v + 2 * k2v + 2 * k3v + k4v) * dt / 6.0
    r = r + (k1r + 2 * k2r + 2 * k3r + k4r) * dt / 6.0
    return r, veltot


# estaba 1240
for i in arange(0, 320):  
    rate(10)
# uranus
    rnewu, velnewu = rk(r, velour, rnp, mu, 1)  
# neptune
    rnewn, velnewn = rkn(rnp, velnp, r, mn, 2)  
# uranus position
    r = rnewu  
# uranus velocity
    velour = velnewu  
    du = mag(r)
# new abgykar velocity of uranus
    omeur = mag(velour) / du  
# angular position uranus
    degr = 205.64 * pi / 180 - omeur * i * dt  
# neptune pos
    rnp = rnewn  
# neptune pos
    velnp = velnewn  
    dn = mag(rnp)
    omenp = mag(velnp) / dn
# radians neptune
    radnp = radnp - dt * omenp  
    npx = dn * cos(radnp)
    npy = dn * sin(radnp)
# neptune position
    rnp = vector(npx, npy, 0)  
    deltaomgs = -omeur + omreal
    graphu.plot(pos=(i, deltaomgs * 180 / pi * 3600))
    urpert.pos = r
# position of arrow on uranus
    fnu.pos = urpert.pos  
# distance Neptune-Uranus
    dnu = mag(rnp - r)  
# axes  the arrow over uranus
    fnu.axis = 75 * norm(rnp - r) / dnu  
# radiovector Neptune
    neptune.pos = rnp  
    fun.pos = neptune.pos
# arrow on neptune
    fun.axis = -fnu.axis  
