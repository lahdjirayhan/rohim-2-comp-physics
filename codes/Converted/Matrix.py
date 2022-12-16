""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Matrix.py:  Matrix multiplication using visual arrays

from vpython import *

# Fill array
vector1 = array([1, 2, 3, 4, 5])  
print((" vector1 =", vector1))
# Add vectors
vector2 = vector1 + vector1  
print(("\n vector2 =", vector2))
# Mult array by scalar
vector2 = 3 * vector1  
print(("\n 3 * vector1 = ", vector2))
# An array of arrays
matrix1 = array(([0, 1], [1, 3]))  
print(("\n matrix1 = \n", matrix1))
print(("\n vector1.shape= ", vector1.shape))
# Matrix multiply
print(("\n matrix1 * matrix1 =\n", matrix1 * matrix1))  
