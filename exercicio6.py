vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i+1} número: "))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]

for numero in vetor:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")
