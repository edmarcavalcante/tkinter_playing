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

janela.mainloop()
