'''
Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B.
'''
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

if x % y == 0:
    print(f"{x} é divisível por {y}")
    
else: 
    print(f"{x} não é divisível por {y}")