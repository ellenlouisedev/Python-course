''' 
1 - O cliente do banco precisa entrar com os seguintes dados: 
  Nome, CPF, 
2 - Mostrar os dados do cliente
3 - Criar uma lista para salvar os dados do cliente
'''

nome = input("Digite o nome: ")
cpf = input("Digite o CPF: ")
dnasc = input("Digite a data da nascimento: ")
tel = input("Digite o telefone: ")

print(f"\nCadastro concluído com sucesso.")

cliente = [nome, cpf, dnasc, tel]
clientes = [cliente]

print('----------------------------------------')

print("Dados do cliente cadastrado: ")
print(f"Nome: {clientes[0][0]}")
print(f"CPF: {clientes[0][1]}")
print(f"Data de nascimento: {clientes[0][2]}")
print(f"Telefone: {clientes[0][3]}")

print('----------------------------------------')