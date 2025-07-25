import numpy as np
import matplotlib.pyplot as plt

R=2 #@param {type:"number"}
d=0.05 #@param {type:"number"}
step=0.8 #@param {type:"number"}
c=0.55 #@param {type:"number"}
g=9.81 #@param {type:"number"}
H=2.75 #@param {type:"number"}
t0 = 0
tf = 100
A0 = np.pi*(d/2)**2


def f(x, y):
  return - c * A0 * np.sqrt(2 * g * y) / (np.pi * (2 * R * y - y**2))

# Runge-Kutta 4to orden
def runge_kutta(x0, y0, xf, h):
    n = int((xf - x0)/step)
    # x2 = np.arange(x0, xf + h, h)
    x = np.linspace(x0, xf, n+1)
    # y2 = np.zeros(len(x))
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = h*f(x[i], y[i])
        k2 = h*f(x[i] + h/2, y[i] + 1/2 * k1)
        k3 = h*f(x[i] + h/2, y[i] + 1/2 * k2)
        k4 = h*f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return x, y

t, h = runge_kutta(t0, H, tf, step)

plt.plot(t, h)
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.title('Descarga de tanque esférico (Runge-Kutta)')
plt.grid()
plt.show()