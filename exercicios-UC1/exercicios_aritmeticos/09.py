'''
Faça um algoritmo para ler três números e se estes poderem formar um triângulo dizer se o triângulo é “Equilátero”, “Isóceles” OU “Escaleno”.
'''

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print("O triângulo é EQUILÁTERO")
    elif x == y or x == z or y == z:
        print("O triângulo é ISÓSCELES")
    else:
        print("O triângulo é ESCALENO")
else:
    print("Os números informados não podem formar um triângulo.")