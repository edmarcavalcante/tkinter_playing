import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Sistema de Gestão")
janela.geometry("400x300")

tk.Label(janela, text="Bem-vindo ao Sistema de Gestão", font=("Arial", 16)).pack(pady=20)

tk.Label(janela, text = "Nome do Aluno: ").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text = "Nota 1: ").pack()
entrada_nota1 = tk.Entry(janela)
entrada_nota1.pack()

tk.Label(janela, text = "Nota 2: ").pack()
entrada_nota2 = tk.Entry(janela)
entrada_nota2.pack()



tabela = ttk.Treeview(janela, columns=("Nome", "Nota 1", "Nota 2", "Média","Situação"), show="headings")

tabela.heading("Nome",text="Nome do Aluno")
tabela.heading("Nota 1", text="Nota 1")
tabela.heading("Nota 2", text="Nota 2")
tabela.heading("Média", text="Média")
tabela.heading("Situação", text="Situação")
tabela.pack()

scrollbar = ttk.Scrollbar(janela, orient="vertical", command=tabela.yview)
tabela.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")


alunos_iniciais = [
    ("Alice", 8.5, 7.0),
    ("Bob", 7.5, 9.8),
    ("Charlie", 6.0, 8.2),
    ("David", 9.0, 6.5),
    ("Eva", 8.2, 7.5),
]

for aluno in alunos_iniciais:
    nome, nota1, nota2 = aluno
    media = nota1 + nota2 / 2
    situacao = "Aprovado" if media >=7 else "Recuperação" if media >=5 else "Reprovado"
    tabela.insert("", "end", values=(nome, nota1, nota2, media, situacao))

#def adicionar_aluno(nome, nota1, nota2):
def adicionar_aluno(event=None):
    nome = entrada_nome.get()
    nota1 = float(entrada_nota1.get())
    nota2 = float(entrada_nota2.get())
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"

    tabela.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))

    entrada_nome.delete(0, 3)
    entrada_nota1.delete(0, tk.END)
    entrada_nota2.delete(0, tk.END)


enviar = tk.Button(janela, text="Enviar", background="yellow")
enviar.bind("<Button-1>", adicionar_aluno)
enviar.pack(side= "top")






janela.mainloop()
