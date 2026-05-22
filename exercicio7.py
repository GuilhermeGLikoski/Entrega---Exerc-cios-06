vetor = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(num)

maior = vetor[0]
posicao_maior = 0

for indice in range(10):
    if vetor[indice] > maior:
        maior = vetor[indice]
        posicao_maior = indice

print(f"Vetor: {vetor}")
print(f"Maior elemento: {maior}")
print(f"Posição (índice) do maior: {posicao_maior}")
