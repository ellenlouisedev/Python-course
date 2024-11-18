'''
Nova fase criando a lista de produtos (CRUD):
- [X] Criar uma lista de produtos e salvar em arquivo txt
- [X] Carregar a lista de produtos de um arquivo txt;
- [X] Atualizar a lista adicionando novos produtos;
- [X] Deletar um produto da lista
'''

produtos = {
    'Arroz': 5.90, 
    'Macarrão': 3.60,
    'Feijão': 8.50,
    'Carne': 50.90,
    'Frango': 20.00,
    'Leite': 4.20,
    'Ovos': 6.80,
    'Tomate': 4.50,
    'Cebola': 3.20,
    'Batata': 2.50,
    'Queijo': 15.90,
    'Açúcar': 3.00,
    'Café': 12.50,
    'Manteiga': 9.40,
    'Pão': 2.80
}

carrinho = []

def mostrar_produtos():
    print('Produtos Disponíveis:')
    for produto, valor in produtos.items():
        print(f"{produto}: R$ {valor}")

def adicionar_produto(total_compras):
    adicione = input("Digite o nome do produto: ")
    if adicione in produtos:
        carrinho.append(adicione) # Adiciona o produto ao carrinho
        total_compras += produtos[adicione] # Soma o valor dos produtos adicionados
        print(f'{adicione} adicionado ao carrinho. Total até o momento: R$ {total_compras}')
    else:
        print("Produto não encontrado. Tente novamente.")
    return carrinho, total_compras

def remover_produto(total_compras):
    if not carrinho:
        print("Carrinho está vazio. Não há produtos para remover.")
        return carrinho, total_compras
    
    produto_remover = input("Digite o nome do produto para remover: ")
    if produto_remover in carrinho:
        carrinho.remove(produto_remover)
        total_compras -= produtos[produto_remover] # Subtrai o valor do produto removido
        print(f'{produto_remover} removido do carrinho. Total até o momento: R$ {total_compras:.2f}')
    else:
        print(f'O produto {produto_remover} não está no carrinho.')
    
    return carrinho, total_compras

def mostrar_menu():
    total_compras = 0.0
    menu = """
    Escolha uma opção dos produtos: 
    [m] Mostrar [a] Adicionar [c] Carrinho
    [r] Remover produto [s] Salvar
    [l] ler o carrinho de compras
    f -(Finalizar Compra)
    """
    while True:
        opcao = input(menu)
        if opcao == 'm':
            mostrar_produtos()
        elif opcao == 'a':
            carrinho, total_compras = adicionar_produto(total_compras)
        elif opcao == 'c':
            print("Produtos no carrinho:")
            for produto in carrinho:
                print(produto)
        elif opcao == 'r':
            carrinho, total_compras = remover_produto(total_compras)
        elif opcao == 's':
            salvar_lista(carrinho, total_compras)
            print("Lista salva com sucesso!")
        elif opcao == 'l':
            carrinho, total_compras = carregar_lista()
            print("Lista carregada com sucesso!")
        elif opcao == 'f':
            print("\nProdutos escolhidos:", ', '.join(carrinho))      
            print(f"Total da compra: R$ {total_compras}")
            break

def salvar_lista(carrinho, total_compras):
    with open("Exercicios-uc2/lista_compras.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Produtos escolhidos: {', '.join(carrinho)}\n")
        arquivo.write(f"Total da compra: R$ {total_compras}")

def carregar_lista():
    try:
        with open("Exercicios-uc2/lista_compras.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            carrinho = linhas[0].split(": ")[1].split(", ")
            total_compras = float(linhas[1].split(": R$ ")[1])
            return carrinho, total_compras
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return [], 0.0
    except IOError:
        print("Erro ao ler o arquivo")
        return [], 0.0

mostrar_menu()