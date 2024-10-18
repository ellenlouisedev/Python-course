'''
Faça um algoritmo para ler os catetos de um triângulo retângulo e calcular e imprimir a sua hipotenusa.
'''
x = int(input())
y = int(input())
 
x = x % y
x = x % y
y = y % x
 
print(y)
