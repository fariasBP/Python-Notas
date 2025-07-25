# OPERADORES BIT A BIT
#     Un operador bit a bit se utiliza para realizar operaciones bit a bit en
#     variables. Devuelve un valor booleano (true o false) basado en la condición.
#     OPERADORES:
#         - & ---> And
#         - | ---> Or
#         - ^ ---> Xor
#         - ~ ---> Not
#         - >> ---> Desplazamiento a la derecha
#         - << --> Desplazamiento a la izquierda
#      EJEMPLO: Consideremos a = 2 (en binario = 10) y b = 3 (en binario = 11) para los siguientes casos.
#         &	Realiza bit a bit la operación AND en los operandos	a & b = 2 (Binario: 10 & 11 = 10)
#         |	Realiza bit a bit la operación OR en los operandos	a | b = 3 (Binario: 10 | 11 = 11)
#         ^	Realiza bit a bit la operación XOR en los operandos	a ^ b = 1 (Binario: 10 ^ 11 = 01)
#         ~	Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando	~a = -3 (Binario: ~(00000010) = (11111101))
#         >>	Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha	a >> b = 0 (Binario: 00000010 >> 00000011 = 0)
#         <<	Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha	a << b = 16 (Binario: 00000010 << 00000011 = 00001000)

a = 2; b=11

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a >> b)
print(a << b)