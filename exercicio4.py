vetor = []

for i in range(8):
    valor = float(input(f"digite o valor para a posição {i}: "))
    vetor.append(valor)

x = int(input("digite o indice X (de 0 a 7): "))
y = int(input("digite o indice Y (de 0 a 7): "))

soma = vetor[x] + vetor[y]
print(f"a soma dos valores nas posições {x} e {y} é: {soma}")
