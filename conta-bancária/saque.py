'''
Receba o valor do saque e compare com o saldo da conta bancária
'''

saldo_inicial = 1000
print('---------------------------------------------')
print (f"Você tem R$ {saldo_inicial} de saldo na conta bancária.")
print('---------------------------------------------')

saldo = saldo_inicial
saque = float(input("Digite o valor do saque: "))

if saque <= saldo:
    print ("Saque realizado com sucesso!")
    saldo = saldo_inicial - saque
    
else:
    print ("Saldo insuficiente!")
    
print (f"Saldo atual: {saldo}")