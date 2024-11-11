'''
Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou impar.
'''
x = int(input("Digite o primeiro número : "))
y = int(input("Digite o segundo número: "))

if x > y:
    print (f"O maior número é {x}")
    print (f"O menor número é {y}")

elif x < y:
    print(f"O maior número é {y}")
    print(f"O menor número é {x}")
    
else:
    print("Os números são iguais")