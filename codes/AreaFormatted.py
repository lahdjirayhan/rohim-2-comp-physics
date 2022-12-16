""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# AreaFormatted: Python 2 or 3 formated output, keyboard input, file input

from numpy import *
from sys import version

# Python 3 uses input, not raw_input
if int(version[0]) > 2:  
    raw_input = input
# raw_input strings
name = eval(input("Key in your name: "))  
print(("Hi ", name))
# For numerical values
radius = eval(input("Enter a radius: "))  
# formatted output
print(("you entered radius= %8.5f" % radius))  
# raw_input  strings
print("Enter new name and r in file Name.dat")  
# Read from file Name.dat
inpfile = open("Name.dat", "r")  
for line in inpfile:
# Splits components of line
    line = line.split()  
# First entry in the list
    name = line[0]  
# print Hi + first entry
    print((" Hi  %10s" % (name)))  
# convert string to float
    r = float(line[1])  
# convert to float & print
    print((" r = %13.5f" % (r)))  
inpfile.close()
A = math.pi * r**2
print("Done, look in A.dat\n")
outfile = open("A.dat", "w")
outfile.write("r=  %13.5f\n" % (r))
outfile.write("A =  %13.5f\n" % (A))
outfile.close()
# Screen output
print(("r = %13.5f" % (r), ", A = %13.5f" % (A)))  
print("\n Now example of integer input ")
age = int(eval(input("Now key in your age as an integer:  ")))
print(("age: %4d  years old,  you don't look it!\n" % (age)))
print("Enter and return a character to finish")
s = eval(input())
