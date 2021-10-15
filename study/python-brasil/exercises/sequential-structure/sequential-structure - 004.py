# 004 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print(f'Média: {sum(list(float(input(f"Nota Nº {i + 1}: ")) for i in range(4))) / 4}')