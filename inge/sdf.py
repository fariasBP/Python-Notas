from itertools import combinations
from functools import reduce
import operator
import numpy as np

print('Producto de binomios:\n(x+a1)(x+a2)(x+a3)...(x+a4)')
# Tu lista de constantes (arr) y su tamaño
print('Ingrese el numero de binomios: ')
n = int( input('n= '))
arr = np.arange(0,n)
for i in range(n):
    print(f'Ingrese el valor de a{i+1}:')
    arr[i] = int( input())
print(arr)

# Lista para guardar C1, C2, ..., Cn
coeficientes = []

for k in range(1, n + 1):
    suma = 0
    for comb in combinations(arr, k):
        producto = reduce(operator.mul, comb, 1)  # Multiplica todos los elementos de la combinación
        suma += producto
    coeficientes.append(suma)

# Imprimir los coeficientes  
print('El resultado sera de la forma x^n + C1x^(n-1) + C2x^(n-2) + C3x^(n-3) + ... + Cnx, donde:')
for i, c in enumerate(coeficientes, 1):
    print(f"C{i} = {c}")
    
