vetor = []
quant_negativos = 0
soma_positivos = 0

for i in range(10):
    numero = float(input(f"Digite o {i+1} número real: "))
    vetor.append(numero)
    
    if numero < 0:
        quant_negativos += 1
    elif numero > 0:
        soma_positivos += numero

print(f"Quantidade de números negativos: {quant_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
