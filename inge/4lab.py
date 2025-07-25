# LAB 4 MECANICA DE FLUIDOS: DESCARGA DEL ORIFICIO

# Problema 25.20 CHAPRA, PAGINA 683 7ma edicion-RUNGE KUTTA

import numpy as np
import matplotlib.pyplot as plt



# definamos las constantes y parametros iniciales
R = 1.5 # m
d = 0.03
step = 0.01
c = 0.55
g = 9.81 # m/s2
Ao = np.pi*(d/2)**2 # m2
H = 2.75 # m
t0 = 0
tf = 100

def descarga(y):
    return - c*Ao*np.sqrt(2*g*y)/(np.pi*(2*R*y-y**2))
    

n = int((tf - t0)/step) # cantidad de ciclos 

t = np.linspace(t0, tf, n+1)

h_m = np.zeros(n+1) # matriz vacia para rellenar h en n veces
h_m[0] = H

for i in range(n):
    # print(i)
    k1 = descarga(h_m[i])
    k2 = descarga(h_m[i] + (step/2)*k1)
    k3 = descarga(h_m[i] + (step/2)*k2)
    k4 = descarga(h_m[i] + step*k3)
    h_m[i+1] = h_m[i] + (1/6*(k1 + 2*k2 + 2*k3 + k4))
    
plt.plot(t, h_m)
plt.grid()
plt.xlabel("tiempo t [s]")
plt.ylabel("altura h [m]")
plt.title("Descarga hidráulica de tanque esférico")
plt.show()
