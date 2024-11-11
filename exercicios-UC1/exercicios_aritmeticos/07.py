# Faça um algoritmo para ler três números e imprimir o maior.

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x > y and x > z:
    print(f"O número é {x}")
    
elif y > x and y > z:
    print(f"O maior número é {y}")
    
else:
    print(f"O maior número é {z}")