import sqlite3
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

# Caminho do banco de dados
ROOT_PATH = Path(__file__).parent
data_path = ROOT_PATH / 'data'

# Função para conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect(data_path / 'banco_de_dados.db')

# Função para inserir dados no banco
def inserir_cliente(nome, email):
    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        conexao.close()
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        limpar_campos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao inserir dados: {e}")

# Função para limpar os campos de entrada
def limpar_campos():
    nome_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Função chamada ao clicar no botão "Cadastrar"
def cadastrar_cliente():
    nome = nome_entry.get()
    email = email_entry.get()

    if not nome or not email:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    inserir_cliente(nome, email)

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("300x200")

# Label e campo para o nome
nome_label = tk.Label(root, text="Nome:")
nome_label.pack(pady=5)
nome_entry = tk.Entry(root, width=30)
nome_entry.pack(pady=5)

# Label e campo para o email
email_label = tk.Label(root, text="Email:")
email_label.pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Botão para cadastrar cliente
cadastrar_button = tk.Button(root, text="Cadastrar", command=cadastrar_cliente)
cadastrar_button.pack(pady=10)

# Rodar a interface gráfica
root.mainloop()