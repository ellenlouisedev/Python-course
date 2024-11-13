import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para conectar ao banco de dados SQLite
def conectar_bd():
    conn = sqlite3.connect('escola.db')  # Conecta ao banco de dados (ou cria um novo)
    return conn

# Função para criar a tabela de alunos no banco de dados (se não existir)
def criar_tabela():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                        matricula TEXT PRIMARY KEY,
                        nome TEXT NOT NULL,
                        curso TEXT NOT NULL,
                        data_nascimento TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Função para cadastrar um aluno no banco de dados
def cadastrar_aluno(nome, matricula, curso, data_nascimento):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO alunos (matricula, nome, curso, data_nascimento) VALUES (?, ?, ?, ?)", 
                       (matricula, nome, curso, data_nascimento))
        conn.commit()
        messagebox.showinfo("Cadastro", "Aluno cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Já existe um aluno com essa matrícula.")
    finally:
        conn.close()

# Função para consultar um aluno pelo número de matrícula
def consultar_aluno(matricula):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE matricula=?", (matricula,))
    aluno = cursor.fetchone()
    conn.close()
    return aluno

# Função para listar todos os alunos
def listar_alunos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos ORDER BY nome")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

# Função para excluir um aluno pelo número de matrícula
def excluir_aluno(matricula):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE matricula=?", (matricula,))
    conn.commit()
    conn.close()

# Função para mostrar os alunos cadastrados em um popup
def exibir_lista_alunos():
    alunos = listar_alunos()
    if not alunos:
        messagebox.showinfo("Lista de Alunos", "Nenhum aluno cadastrado!")
        return

    alunos_lista = "Nome - Matrícula\n" + "-"*30 + "\n"
    for aluno in alunos:
        alunos_lista += f"{aluno[1]} - {aluno[0]}\n"  # nome e matrícula

    messagebox.showinfo("Lista de Alunos", alunos_lista)

# Função de cadastro do aluno
def on_cadastrar():
    nome = entry_nome.get()
    matricula = entry_matricula.get()
    curso = entry_curso.get()
    data_nascimento = entry_data_nascimento.get()

    if nome and matricula and curso and data_nascimento:
        cadastrar_aluno(nome, matricula, curso, data_nascimento)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

# Função de consulta de aluno
def on_consultar():
    matricula = entry_consulta_matricula.get()
    aluno = consultar_aluno(matricula)
    if aluno:
        messagebox.showinfo("Aluno Encontrado", f"Nome: {aluno[1]}\nMatrícula: {aluno[0]}\nCurso: {aluno[2]}\nData de Nascimento: {aluno[3]}")
    else:
        messagebox.showerror("Erro", "Aluno não encontrado.")

# Função de exclusão de aluno
def on_excluir():
    matricula = entry_excluir_matricula.get()
    aluno = consultar_aluno(matricula)
    if aluno:
        excluir_aluno(matricula)
        messagebox.showinfo("Exclusão", "Aluno excluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Aluno não encontrado.")

# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Sistema de Cadastro de Alunos")

# Frame de Cadastro
frame_cadastro = tk.Frame(root)
frame_cadastro.pack(padx=10, pady=10)

label_nome = tk.Label(frame_cadastro, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=0, column=1)

label_matricula = tk.Label(frame_cadastro, text="Matrícula:")
label_matricula.grid(row=1, column=0)
entry_matricula = tk.Entry(frame_cadastro)
entry_matricula.grid(row=1, column=1)

label_curso = tk.Label(frame_cadastro, text="Curso:")
label_curso.grid(row=2, column=0)
entry_curso = tk.Entry(frame_cadastro)
entry_curso.grid(row=2, column=1)

label_data_nascimento = tk.Label(frame_cadastro, text="Data de Nascimento (dd/mm/yyyy):")
label_data_nascimento.grid(row=3, column=0)
entry_data_nascimento = tk.Entry(frame_cadastro)
entry_data_nascimento.grid(row=3, column=1)

btn_cadastrar = tk.Button(frame_cadastro, text="Cadastrar Aluno", command=on_cadastrar)
btn_cadastrar.grid(row=4, column=0, columnspan=2)

# Frame de Consulta
frame_consulta = tk.Frame(root)
frame_consulta.pack(padx=10, pady=10)

label_consulta_matricula = tk.Label(frame_consulta, text="Digite a matrícula para consultar:")
label_consulta_matricula.grid(row=0, column=0)
entry_consulta_matricula = tk.Entry(frame_consulta)
entry_consulta_matricula.grid(row=0, column=1)

btn_consultar = tk.Button(frame_consulta, text="Consultar Aluno", command=on_consultar)
btn_consultar.grid(row=1, column=0, columnspan=2)

# Frame de Exclusão
frame_exclusao = tk.Frame(root)
frame_exclusao.pack(padx=10, pady=10)

label_excluir_matricula = tk.Label(frame_exclusao, text="Digite a matrícula para excluir:")
label_excluir_matricula.grid(row=0, column=0)
entry_excluir_matricula = tk.Entry(frame_exclusao)
entry_excluir_matricula.grid(row=0, column=1)

btn_excluir = tk.Button(frame_exclusao, text="Excluir Aluno", command=on_excluir)
btn_excluir.grid(row=1, column=0, columnspan=2)

# Botão para listar alunos
btn_listar = tk.Button(root, text="Listar Alunos", command=exibir_lista_alunos)
btn_listar.pack(padx=10, pady=10)

# Inicializa o banco de dados e cria a tabela de alunos
criar_tabela()

# Inicia a interface gráfica
root.mainloop()