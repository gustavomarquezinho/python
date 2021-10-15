# 013 - Tendo como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: (Homens: (72.7 * H) - 58 | Mulheres: (62.1 * H) - 44.7).

heightValue = float(input('Altura: '))
print(f'\nHomens: {72.7 * heightValue - 58:.2f}kg\nMulheres: {62.1 * heightValue - 44.7:.2f}kg\n')