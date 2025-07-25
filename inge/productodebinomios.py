#vamos a multilicar producto de binomios
import numpy as np
print('Producto de binomios:\n(x+A)(x+B)(x+C)...(x+L)')
print('Ingrese el numero de binomios: ')
n = int( input('n= '))
if n > 12:
    print('El numero de binomios es demasiado grande')
    exit()
arr = np.arange(0,n)
vr = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
for i in range(n):
    print('Ingrese el valor de', vr[i], ': ')
    arr[i] = int( input())
print(arr) #[1,2,3]

# C1 = 0
# for i in range(n):
#     C1 = C1 + arr[i]
# print(C1)

# C2=0
# for i in range(n):
#     for j in range(i+1,n):
#         C2 = C2 + arr[i]*arr[j] 
# print(C2)

# C3=0
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             C3 = C3 + arr[i]*arr[j]*arr[k]
# print(C3)

# C4=0
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 C4 = C4 + arr[i]*arr[j]*arr[k]*arr[l]
# print(C4)
    

arr2=np.arange(0,n)
for i in range(n):
    arr2[i] = arr2[i] + arr[i]
    print(C1)
    if n > 2:
        for j in range(i+1,n):
            C2 = C2 + arr[i]*arr[j]
            print(C2)
            if n > 3:
                for k in range(j+1,n):
                    C3 = C3 + arr[i]*arr[j]*arr[k]
                    print(C3)
                    if n > 4:
                        for l in range(k+1,n):
                            C4 = C4 + arr[i]*arr[j]*arr[k]*arr[l]
                            print(C4)
                            if n > 5:
                                for m in range(l+1,n):
                                    C5 = C5 + arr[i]*arr[j]*arr[k]*arr[l]*arr[m]
                                    print(C5)
                                    if n > 6:
                                        for n in range(m+1,n):
                                            C6 = C6 + arr[i]*arr[j]*arr[k]*arr[l]*arr[m]*arr[n]
                                            print(C6)
                                            if n > 7:
                                                for o in range(n+1,n):
                                                    C7 = C7 + arr[i]*arr[j]*arr[k]*arr[l]*arr[m]*arr[n]*arr[o]
                                                    print(C7)
                                                    if n > 8:
                                                        for p in range(o+1,n):
                                                            C8 = C8 + arr[i]*arr[j]*arr[k]*arr[l]*arr[m]*arr[n]*arr[o]*arr[p]
                                                            print(C8)
                                                            if n > 9:
                                                                for q in range(p+1,n):
                                                                    C9 = C9 + arr[i]*arr[j]*arr[k]*arr[l]*arr[m]*arr[n]*arr[o]*arr[p]*arr[q]
                                                                    print(C9)
                                                                    if n > 10:
                                                                        for r in range(q+1,n):
                                                                            C10 = C10 + arr[i]*arr[j]*arr[k]*arr[l]*arr[m]*arr[n]*arr[o]*arr[p]*arr[q]*arr[r]
                                                                            print(C10)
                                                                            if n > 11:
                                                                                for s in range(r+1,n):
                                                                                    C11 = C11 + arr[i]*arr[j]*arr[k]*arr[l]*arr[m]*arr[n]*arr[o]*arr[p]*arr[q]*arr[r]*arr[s]
                                                                                    print(C11)
                                                                                    if n > 12:
                                                                                        for t in range(s+1,n):
                                                                                            C12 = C12 + arr[i]*arr[j]*arr[k]*arr[l]*arr[m]*arr[n]*arr[o]*arr[p]*arr[q]*arr[r]*arr[s]*arr[t]
                                                                                            print(C12)