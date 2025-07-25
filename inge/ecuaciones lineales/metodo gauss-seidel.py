import numpy as np
print("METODO GAUSS-SEIDEL\n")
eqts = np.array([[0, -2/5, -1/5, 1/5],[0, 0, 2/3, 0],[ 4/6, 1/6, 0, -1/6]]) # se coloca la matriz despejada

n = 10 # colocas el numero de iteraciones

vars = 3 # colocas el numero de variables


list = np.zeros((n+1, vars))

for i in range(1, n+1):
    list[i] = list[i-1].copy() 
    for j in range(vars):
        s = 0
        for m in range(vars):
            if m != j:
                s = s + eqts[j][m]*list[i][m]
        list[i][j] = s + eqts[j][vars]

print(list)