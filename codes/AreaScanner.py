""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# AreaScanner: examples of use of formated output
# and  reading input from the keyboard. Also: Input/Output with files

import math

# raw_input is good for strings
name = eval(input("Key in your name: "))  
print(("Hi ", name))
# works with numerical values
radius = eval(input("Enter a radius: "))  
# formatted output
print(("you entered radius= %8.5f" % radius))  
# raw_input good for strings
name = eval(input("Key in another name: "))  
radius = eval(input("Enter a radius: "))
print("Enter new name and r in file Name.dat")
# to read from file Name.dat
inpfile = open("Name.dat", "r")  
for line in inpfile:
# splits components of line
    line = line.split()  
# first entry in the list
    name = line[0]  
# print Hi plus first entry
    print((" Hi  %10s" % (name)))  
# second entry convert to float
    r = float(line[1])  
# converts x to float and print it
    print((" r = %13.5f" % (r)))  
inpfile.close()
# use radius to find circles's area
A = math.pi * r**2  
print("Done, look in A.dat\n")
outfile = open("A.dat", "w")
outfile.write("r=  %13.5f\n" % (r))
outfile.write("A =  %13.5f\n" % (A))
outfile.close()
# screen output
print(("r = %13.5f" % (r)))  
print(("A = %13.5f" % (A)))
print("Now example of integer input ")
age = int(eval(input("Now key in your age as an integer:  ")))
print(("age: %4d  years old,  you don't look it!\n" % (age)))
print("Press a character to finish")
s = eval(input())
