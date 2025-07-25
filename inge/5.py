# Created on Wed Dec  4 23:47:08 2024

# @author: DELL

# Mec_tema5_algebra de matricesss

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# PYTHON MATRICES AND NUMPY ARRAYS
#https://www.programiz.com/python-programming/matrix

## Python Programs the BEST!!!!!!!!!!!!!!!!!! MTRICES 
## https://www.geeksforgeeks.org/python-programming-examples/?ref=outindfooter

##Hans-Petter Halvorsen

## LINEAAR ALGEBRA https://numpy.org/doc/stable/reference/routines.linalg.html
# NumPy Array
A = np.array([[1, 3, 7, 2], 
[5, 8, -9, 0],
[6, -7, 11, 12]])
print("A =", A) 

# Numpy Matrix
A = np.matrix([[1, 3, 7, 2], 
[5, 8, -9, 0],
[6, -7, 11, 12]])
print("A =", A) 

# NumPy.matrix
A = np.matrix([[0, 1], 
              [-2, -3]])
B = np.matrix([[1, 0], 
              [3, -2]])
# Suma de matrices, adición y multiplicacion, CASO DataFrame
C = A + B
print("A+B =", C)
C = A - B
print("A-B =", C)
C = A * B
print("A*B =", C)

C = np.mat(A) * np.mat(B)
print("A*B =", C)

C = np.matmul(A,B)
print ("A*B = ", C)

# Transpose of a Matrix
A = np.array([[1, 3, 7, 2], 
[5, 8, -9, 0],
[6, -7, 11, 12]])
print("A="); print(A)
Atr = np.transpose(A)
print("Transpose of A="); print(Atr)

# Program to add two matrices using nested loop, tipy matrices list
## https://www.geeksforgeeks.org/python-program-add-two-matrices/

## Matrices list and reslut in list

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
#d = len(X) da 3 filas
Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X[0:2])): # lee para X 3 filas 
    # iterate through columns
    for j in range(len(X[0:2])): # j avanza para cada fila empezando de 0
        result[i][j] = X[i][j] + Y[i][j]
print (result) # hasta aqui ya realiza la suma 
for k in result: # En la matriz Result leerá cada fila conociendo ya 3 columnas
    print(k)

# Suma de matrices list de otra forma, ejecurta normal 
for i in range (len(X)):
    for j in range (len(Y)):
        result[i][j] = X[i][j] + Y[i][j]
print (result)

### con for k
for i in range(len(X[0:2])): # lee para X 3 filas 
    # iterate through columns
    for j in range(len(X[0:2])): # j avanza para cada fila empezando de 0
        result[i][j] = X[i][j] + Y[i][j]
#print (result) # hasta aqui ya realiza la suma 
for k in result:
    print(k)


# Add Two Matrices Using SymPy
from sympy import Matrix
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Create Matrix objects from the lists
matrix_x = Matrix(X)
matrix_y = Matrix(Y)

# Add the matrices
result = matrix_x + matrix_y
# Print the result
print(result)
 
# https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
## Python Program to Multiply Two Matrices list

matrix_a = [[1,2], 
            [3,4]] # i*k 
matrix_b = [[5,6], 
            [7,8]] # k*j
result = [[0,0], # i*j
          [0,0]]

for i in range (2):
    for j in range (2):
        result[i][j] = (matrix_a[i][0] * matrix_b[0][j]+
                        matrix_a[i][1] * matrix_b[1][j])
 
for k in result:
    print (k, result)


#Cambiando rang2
matrix_a = [[1, 2], 
            [3, 4]] 
matrix_b = [[5, 6], 
            [7, 8]]

result = [[0, 0], 
          [0, 0]]

for i in range(len(matrix_a[0:2])):
    for j in range(len(matrix_b[0:2])):
        result[i][j] = (matrix_a[i][0] * matrix_b[0][j] +
                        matrix_a[i][1] * matrix_b[1][j])

for row in result:
    print(row, result)

# iterating by row of A# take a 3x3 matrix
# Multiply two matrices usng Nested Loops

A = [[12, 7, 3],        # i*k A = 3*3
    [4, 5, 6],
    [7, 8, 9]]

# take a 3x4 matrix    
B = [[5, 8, 1, 2],      # k*j # B = 3*4
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
    
result = [[0, 0, 0, 0],  # result = A[i][k]*B[k][j] ;    result = 3*4
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
# Iterating by row of A
for i in range(len(A)):
    # iterating by column by B 
    for j in range(len(B[0])):
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)

# Matrix multiplication using NumPy
import numpy as np

# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

# result will be 3x4

result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

result = np.dot(A,B)
print (result)

for r in result:
    print(r)

# Print the result
print(result)

### work with a nested list https://www.programiz.com/python-programming/matrix
## Only for list format and read list !!!!!!!!!!!!!!!!!
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

# Para leer filas o elementos de matriz lista 
print("A =", A) 
# Leer la 1ra columna de la lista 
print("A[0]=", A[0])# Lee toda la fila 0 de la lista
print("A[0]=", A[0][:])

print ("A[2]=", A[2][:])
print ("A[2]=", A[2])
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row
print("A[0][0:4] =", A[0][0:4]) 

# Sacar el valor de 19 de A
print("A[2][-1] =", A[2][-1])
print("A[2][3] =", A[2][3])

print("A[1][2] =", A[1][2])   # 3rd element of 2nd row =9


print("A[0] =", A[:][0])# NO lee una columna lista de esta manera
#print("B[:,0] =", B[:,0]) esta forma no lee por ser lista la matriz
print("A[:,0] =", A[:,0]),# no lee 


# Para leer la columna de matris lista, de otra form no se puede
# La forma para leer una matriz, de otra forma no se puede leer, es lista!
column = [];        # empty list, para leer columna en una matris lista 
for i in (A): # lee las 3 filas completas 
  column.append(i[0])  # de la fila i=0 toma el valor de la columna 0 =1 
                       # luego para i=1, siguiente valor de la coumna 0 = -5
                       # luego para i=2, siguiente valor de la columna 0=-6               
print(column)
                       # Resultado, 5,9,11

# Leer columna 0 de otra forma con pandas de una matris lista 
import pandas as pd
column_1 = []
for i in (A):
    column_1.append(i[1])
print ("Column_1= ", column_1)

## Leer 3r columna de una matriz lista
terceraColumna = []
for k in (A): # lee todas las filas 
    terceraColumna.append(k[3])
print ("#racolumna =", terceraColumna)

# Ahora uso de np para escribir matrices leer valores, filas y columnas
# Aqui siempre se elijen pares: i y j
import numpy as np
B = np.array([[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])
# lee la 1ra columna [1 -5 -6]
print("B[:,0] =", B[:,0]) # First Column, puede leer si solo la matriz esta en np

# Lee la 3ra columna
print("B[:,3] =", B[:,3])  # lee la 3ra columna

# 3rd element of 2nd row = 9
print("B[1][2] =", B[1][2])   # 3rd element of 2nd row = 9

print("B[0]=", B[0])# lee todo la 1ra fila
print("B[0]=", B[0][:])# lee todo la 1ra fila
print("B[0]=", B[0][0:4])# lee todo la 1ra fila

print ("Lee la 2da fila = ", B[1])# lee toda la 2da fila 
print ("lee las dos 1ras filas = ", B[0:2])# lee las 2 1ras filas
                                           # pero el limite debe ser hasta 2
print ("lee las dos 1ras filas = ", B[0:3]) # Como es solamente es [], entonces solo puede ser filas

print ("lee el 1er valor de B=", B[0][0])
print ("lee la 1ra fila =", B[0:1])# 1 es hasta la fila x y lee la fila 0
print ("n al forma siguiente no hace nada =", B[0:0]) # no hay límite superior
print ("n al forma siguiente no hace nada =", B[0][0])# aqui vale ya que se eleije i y j

# Puedo leer toda la matriz?
print ("Toda la matriz= ", B[:,:]) # le toda la matriz DataFrame
print ("Toda matriz de otra forma = ",B[0:3,0:4] ) #lee la matriz DataFrame

# Lectura de la 1ra columna con pd, funciona para una matriz array
# Como se ha visto las filas se podia leer,pero las columnas solo con for
import pandas as pd
column_00 = []
for i in (B): # lee todas las filas
    column_00.append(i[0]) # lee todas las filas y de la 1ra columna
print ("1ra comumn de B=", column_00)

# leer la 2da columna 
import pandas as pd
column_00 = []
for i in (B): # lee todas las filas
    column_00.append(i[1]) # lee todas las filas y de la 1ra columna
print ("1ra comumn de B=", column_00)
