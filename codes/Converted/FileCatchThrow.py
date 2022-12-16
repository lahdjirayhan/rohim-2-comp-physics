""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# FileCatchThrow.py:  throws and catches exception
# program with mistake to see action of exception
import sys
import math

r = 2
# Calculate circum
circum = 2.0 * math.pi * r  
# Calculate A
A = math.pi * r**2  
try:
# Intentional error 'r'
    q = open("ThrowCatch.dat", "w")  
    # Replace r' to 'w', run
except IOError:
    print("Cannot open file")
else:
    q.write("r = %9.6f, length = %9.6f, A= %9.6f " % (r, circum, A))
    q.close()
    print("output in ThrowCatch.out")
    # catch(IOException ex){ex.printStackTrace(); }               # Catch