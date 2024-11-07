# Esse desafio consiste em somar os itens de um lista de compras.

produtos = {'Arroz': 5.90, 
            'Macarrão': 3.60,
            'Feijão': 8.50,
            'Carne': 50.90,
            'Frango':20.00,}

carrinho = []

def mostrar_produtos():
    print('Produtos Disponíveis:')
    for produto, valor in produtos.items():
        print(f"{produto}: R$ {valor}")

def adicionar_produto(total_compras):
    adicione = input("Digite o nome do produto: ")
    if adicione in produtos:
        carrinho.append(adicione) # adiciona o produto ao carrinho
        total_compras += produtos[adicione] # soma o valor doso produtos adicionados
        print(f'{adicione} adicionado ao carrinho. Total até o momento: R$ {total_compras}')
    else:
        print("Produto não encontrado. Tente novamente.")
    return total_compras

def mostrar_menu():
    total_compras = 0.0
    menu = """
    Escolha uma opção dos produtos: 
    m - (Mostrar); a - (Adicionar); c (Carrinho); f - (Finalizar Compra)
    """
    while True:
        opcao = input(menu)
        if opcao == 'm':
            mostrar_produtos()
        elif opcao == 'a':
            total_compras = adicionar_produto(total_compras)
        elif opcao == 'c':
            print("Produtos no carrinho:")
            for produto in carrinho:
                print(produto)
        elif opcao == 'f':
            #Exibindo o Total das Compras depois que apertar 'x'
            print("\nProdutos escolhidos:", ', '.join(carrinho))      
            print(f"Total da compra: R$ {total_compras}")
            break


mostrar_menu()