""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# SU3.py: SU3 matrix manipulations

from numpy import *
from numpy.linalg import *

# eight generators
L1 = array([[0, 1, 0], [1, 0, 0], [0, 0, 0]])  
L2 = array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])
L3 = array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
L4 = array([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
L5 = array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]])
L6 = array([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
L7 = array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])
L8 = array([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) * 1 / sqrt(3)

# up quark
u = array([1, 0, 0])  
# down quark
d = array([0, 1, 0])  
# strange quark
s = array([0, 0, 1])  

# raising operators
Ip = 0.5 * (L1 + 1j * L2)  
Up = 0.5 * (L6 + 1j * L7)
Vp = 0.5 * (L4 + 1j * L5)
# lowering operators
Im = 0.5 * (L1 - 1j * L2)  
Um = 0.5 * (L6 - 1j * L7)
Vm = 0.5 * (L4 - 1j * L5)

# raices d to u
Ipxd = dot(Ip, d)  
print(("\n Ipxd", Ipxd))
# raises s to u
Vpxs = dot(Vp, s)  
print(("\n Vpxs", Vpxs))
#  raises s to d
Upxs = dot(Up, s)  
print(("\n Upxs", Upxs))
