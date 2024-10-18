'''
Faça um algoritmo para ler o preço de compra de uma mercadoria e calcular o seu preço de venda para que possa ser obtido um lucro de 30%.
'''

preco_compra = float(input('Digite o preço de compra da mercadoria: '))
lucro = preco_compra * 0.30
preco_venda = preco_compra + lucro

print ("O preço de venda para obter 30% de lucro é:", preco_venda)