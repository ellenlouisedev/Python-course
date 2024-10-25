saldo = 1000.0  

print (f"Seu saldo atual é: R$ {saldo}")

while True:
    valor_saque = float(input("Digite o valor do saque (ou 'sair' para sair): "))
    
    if valor_saque == 'sair':
        break
    
    if valor_saque <= 0:
        print("O valor do saque tem que ser maior que zero. Tente novamente.")
    elif valor_saque > saldo:
        print(f"Saldo insuficiente. Seu saldo atual é: R$ {saldo}")
    else:
        valor_saque -= saldo
        print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {saldo - valor_saque}")