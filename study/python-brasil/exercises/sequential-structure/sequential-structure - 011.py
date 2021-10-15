# 011 - Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre: 
# A) O produto do dobro do primeiro com metade do segundo; 
# B) A soma do triplo do primeiro com o terceiro;
# C) O terceiro elevado ao cubo.

number1, number2, number3 = int(input('Número inteiro: ')), int(input('Número inteiro: ')), float(input('Número real: '))
print(f'\nDobro do primeiro com metade do segundo: {(number1 * 2) * (number2 / 2)}\nSoma do triplo do primeiro com o terceiro: {(number1 * 3) + number3}\nTerceiro elevado ao cubo: {number3 ** 3}')