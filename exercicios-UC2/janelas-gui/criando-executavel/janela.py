import tkinter as tk

# Criação da janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela")
janela.geometry("300x300")

# Criação de um rótulo
greeting = tk.Label(janela, text="Usando a Interface Gráfica Tkinter",
                    fg="white", 
                    bg="black",
                    width=30,
                    height=5
                    )
greeting.pack(pady=10)

# Criação de um botão
button = tk.Button(janela,
                   text="Clique Aqui",
                   fg="yellow",
                   bg="blue",
                   width=15,
                   height=2,
                   command=lambda: greeting.config(text="Botão clicado!")
                   )
button.pack(pady=10)

# Adicionando uma entrada de texto
entry = tk.Entry(janela, fg="yellow", bg="blue", width=50)
entry.pack(pady=10)

# Botão que altera o texto do rótulo com o texto da entrada
button2 = tk.Button(janela, text="Escreva algo e clique no botão",
                    command=lambda: greeting.config(text=entry.get()),
                    fg="yellow",
                    bg="blue",
                   )
button2.pack(pady=10)

# Botão que apaga o texto do rótulo
button3 = tk.Button(janela, text="Apagar",
                    command=lambda: greeting.config(text=""),
                    fg="yellow",
                    bg="blue",
                   )
button3.pack(pady=10)

# Iniciando o loop principal
janela.mainloop()
