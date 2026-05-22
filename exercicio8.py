notas = []
soma = 0

for i in range(15):
    nota = float(input(f"Digite a nota do {i+1} aluno: "))
    notas.append(nota)
    soma += nota

media = soma / 15
print(f"A média geral das notas é: {media}")
