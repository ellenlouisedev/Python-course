'''
Criar um aplicativo em Python que funcione como um sistema de cadastro de alunos para uma escola.
O sistema deve permitir a inserção, consulta e exclusão de dados dos alunos.
'''

alunos = {}
def menu():
    menu_principal = """
    ==================
    Menu Principal:
    1. Cadastrar Aluno
    2. Consultar Aluno
    3. Excluir Aluno
    4. Sair
    ==================
    
    """
    print(menu_principal)

def escolher_opcao():
    while True:
        opcao = int(input("Digite sua opção: "))
        match(opcao):
            case 1:
                cadastrar_aluno()
            case 2:
                consultar_aluno()
            case 3:
                excluir_aluno()
            case 4:
                break
            case _:
                print("Opção inválida!")
        

def cadastrar_aluno():
    # Cadastrar aluno: Permitir a inserção de dados do aluno, incluindo nome, matrícula, curso e data de nascimento.
        aluno = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        curso = input("Digite o curso do aluno: ")
        data_nascimento = input("Digite a data de nascimento do aluno (dd/mm/yyyy): ")
        print(f"\nAluno {aluno} cadastrado com sucesso!")
        alunos[matricula] = {"nome": aluno, "curso": curso, "data_nascimento": data_nascimento}
        return alunos

def consultar_aluno():
    # Buscar um aluno por matrícula e exibir seus dados completos.
        buscar_matricula = input("Digite a matrícula do aluno que deseja consultar: \n")
        if buscar_matricula in alunos:
            aluno_encontrado = alunos[buscar_matricula]
            print(f"Aluno encontrado: {aluno_encontrado['nome']}")
            print(f"Matrícula: {buscar_matricula}")
            print(f"Curso: {aluno_encontrado['curso']}")
            print(f"Data de Nascimento: {aluno_encontrado['data_nascimento']}")

        else :
            print("Aluno não encontrado!")

def excluir_aluno():
    # Excluir um aluno por matrícula.
    excluir_matricula = input("Digite a matrícula do aluno que deseja excluir: ")
    if excluir_matricula in alunos:
        del alunos[excluir_matricula]
        print(f"Aluno com matrícula {excluir_matricula} excluído com sucesso!")
    else:   
        print("Aluno não encontrado!")
    pass


menu()
escolher_opcao()
# TODO mostrar menu para escolher opções

# TODO criar a função para mostrar os alunos mais organizados
print(alunos.items())