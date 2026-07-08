import exemplo00

def adicionar_aluno(nome, nota1, nota2):
    nome = exemplo00.entrada_nome.get()
    nota1 = exemplo00.entrada_nota1.get()
    nota2 = exemplo00.entrada_nota2.get()
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"

    exemplo00.tabela.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))
    
                                               
                                        

