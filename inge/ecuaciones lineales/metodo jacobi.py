import numpy as np
print("METODO JACOBI\n")
'''
para una matriz de la forma
|5 2 1 ||x1| |1 |
|0 -3 2||x2|=|0 |
|-4 1 6||x3| |-1|
'''
eqts = np.array([[0, -2/5, -1/5, 1/5],[0, 0, 2/3, 0],[ 4/6, 1/6, 0, -1/6]]) # se coloca la matriz despejada

n = 10 # colocas el numero de iteraciones
vars = 3 # colocas el numero de variables

valInit = 0

list = np.zeros((n, vars))

for i in range(n):
    for j in range(vars):
        s = 0
        for m in range(vars):
            if i != 0:
                if m != j:
                    s = s + eqts[j][m]*list[i-1][m]
            else:
                s = s + eqts[j][m]*valInit
        list[i][j] = s + eqts[j][vars]

print(list)