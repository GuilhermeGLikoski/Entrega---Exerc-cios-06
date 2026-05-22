vetor = []
contador_pares = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1} número: "))
    vetor.append(numero)
    
    if numero % 2 == 0:
        contador_pares += 1

print(f"O vetor possui {contador_pares} valores pares.")
