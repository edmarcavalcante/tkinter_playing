import exemplo00

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
    exemplo00.tabela.insert("", "end", values=(nome, nota1, nota2, media, situacao))

    