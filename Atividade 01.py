# 1 - Receber nome e nota de 10 alunos
alunos = []

for i in range(10):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))

# 1.2 - Calcular a média das notas
notas = [nota for nome, notas in alunos]
media = sum(notas) / len(alunos)

# 1.3 - Imprimir a média
print(f"\nMédia da turma: {media:.2f}")


# 1.4 - Maior e menor nota e respectivos alunos
maior_nota = max(notas)
menor_nota = min(notas)

print(f"\nMaior nota: {maior_nota:.2f}")

for nome, nota in alunos:
    if nota == maior_nota:
        print(f" - Aluno: {nome}")

print(f"\nMenor nota: {menor_nota:.2f}")

for nome, nota in alunos:
    if nota == menor_nota:
        print(f" - Aluno: {nome}")

# 1.5 - Alunos abaixo da média
print("\nAlunos com nota abaixo da média:")

for nome, nota in alunos:
    if nota < media:
        print(f"{nome}: {nota:.2f}")

# 1.6 - Alunos com nota maior ou igual à média
print("\nAlunos com nota maior ou igual à média:")

for nome, nota in alunos:
    if nota >= media:
        print(f"{nome}: {nota:.2f}")
