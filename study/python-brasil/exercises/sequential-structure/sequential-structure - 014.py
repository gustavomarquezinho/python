# 014 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor
# da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

while True:
	fishWeight = float(input("Insira o peso em kg: ")) - 50.0
	
	if fishWeight <= -50.0:
		break

	print(f"\nx Multa para {fishWeight}kg excedidos: R${fishWeight * 4.0}\n" if fishWeight > 0.0 else "\n› O limite de 50.0kg não foi ultrapassado!\n")