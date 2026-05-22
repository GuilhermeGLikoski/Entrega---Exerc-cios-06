valores = []
soma = 0

for i in range(5):
    valor = float(input(f"Digite o {i+1} valor: "))
    valores.append(valor)
    soma += valor

maior = valores[0]
menor = valores[0]

for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

media = soma / 5

print(f"Valores lidos: {valores}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media}")
