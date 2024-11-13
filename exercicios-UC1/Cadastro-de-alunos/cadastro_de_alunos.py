# Criar um aplicativo em Python que funcione como um sistema de cadastro de alunos para uma escola.  O sistema deve permitir a inserção, consulta e exclusão de dados dos alunos.

alunos = {}

def menu():
    # Exibe o menu principal do sistema.
    menu_principal = """
    ==================
    Menu Principal:
    1. Cadastrar Aluno
    2. Consultar Aluno
    3. Listar Alunos
    4. Excluir Aluno
    5. Sair
    ==================
    """
    print(menu_principal)

def escolher_opcao():
    # Processa a escolha do usuário e chama as funções correspondentes.
    while True:
        try:
            opcao = int(input("Digite sua opção: "))
            if opcao == 1:
                cadastrar_aluno()
            elif opcao == 2:
                consultar_aluno()
            elif opcao == 3:
                listar_alunos()
            elif opcao == 4:
                excluir_aluno()
            elif opcao == 5:
                print("Programa finalizado com sucesso!")
                break
            else:
                print("Opção inválida! Digite um número entre 1 e 5.")
        except ValueError:
            print("Digite apenas números inteiros!")

def cadastrar_aluno():
    # Cadastra um novo aluno.
    aluno = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    curso = input("Digite o curso do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno (dd/mm/yyyy): ")
    
    # Armazenando as informações no dicionário
    alunos[matricula] = {"nome": aluno, "curso": curso, "data_nascimento": data_nascimento}
    
    print(f"\nAluno {aluno} cadastrado com sucesso!")

def consultar_aluno():
    # Consulta um aluno pelo número de matrícula."""
    buscar_matricula = input("Digite a matrícula do aluno que deseja consultar: \n")
    
    if buscar_matricula in alunos:
        aluno_encontrado = alunos[buscar_matricula]
        print(f"\nAluno encontrado: {aluno_encontrado['nome']}")
        print(f"Matrícula: {buscar_matricula}")
        print(f"Curso: {aluno_encontrado['curso']}")
        print(f"Data de Nascimento: {aluno_encontrado['data_nascimento']}")
    else:
        print("Aluno não encontrado!")
        
def listar_alunos():
    # Exibe a lista de todos os alunos cadastrados, ordenada por nome.
    if not alunos:
        print("\nNenhum aluno cadastrado no sistema!")
        return
    
    print("\n==== LISTA DE ALUNOS CADASTRADOS ====")
    print("--------------------------------------")
    
    # Ordenando os alunos por nome
    alunos_ordenados = dict(sorted(alunos.items(), key=lambda x: x[1]['nome']))
    
    for matricula, dados in alunos_ordenados.items():
        print(f"Nome: {dados['nome']}")
        print(f"Matrícula: {matricula}")
        print(f"Curso: {dados['curso']}")
        print(f"Data de Nascimento: {dados['data_nascimento']}")
        print("--------------------------------------")
    
    print(f"Total de alunos cadastrados: {len(alunos)}")
    print("======================================\n")


def excluir_aluno():
    # Exclui um aluno pelo número de matrícula.
    excluir_matricula = input("Digite a matrícula do aluno que deseja excluir: ")
    
    if excluir_matricula in alunos:
        del alunos[excluir_matricula]
        print(f"Aluno com matrícula {excluir_matricula} excluído com sucesso!")
    else:
        print("Aluno não encontrado!")
        
def iniciar():
    # Função que inicia o programa e chama o menu principal.
    while True:
        menu()
        escolher_opcao()

# Iniciar o sistema
iniciar()