""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# Directives.py illustrates escape and formatting  characters
import sys

print("hello \n")
# tabulator
print("\t it's me")  
b = 73
# for integer
print(("decimal 73 as integer b = %d " % (b)))  
# octal
print(("as octal b = %o" % (b)))  
# works hexadecimal
print(("as hexadecimal b = %x " % (b)))  
# use of double quote symbol
print('learn "Python" ')  
# use of \\
print("shows a backslash \\")  
# print single quotes
print("use of single ' quotes ' ")  
