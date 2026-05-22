vetor_original = []
vetor_quadrados = []

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor_original.append(numero)
    
    quadrado = numero ** 2
    vetor_quadrados.append(quadrado)

print("Vetor Original:", vetor_original)
print("Vetor dos Quadrados:", vetor_quadrados)

#append: é utilizado para adicionar um único elemento sempre ao final de uma lista existente.
