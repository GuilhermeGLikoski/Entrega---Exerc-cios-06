valores = []

for i in range(5):
    valor = float(input(f"Digite o {i+1} valor: "))
    valores.append(valor)

maior = valores[0]
menor = valores[0]
pos_maior = 0
pos_menor = 0

for idx in range(5):
    if valores[idx] > maior:
        maior = valores[idx]
        pos_maior = idx
    if valores[idx] < menor:
        menor = valores[idx]
        pos_menor = idx

print(f"O maior valor está na posição (índice): {pos_maior}")
print(f"O menor valor está na posição (índice): {pos_menor}")
