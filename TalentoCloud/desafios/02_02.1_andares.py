"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
"""

#saber quantos andares tem o prédio

andares=int(input("quantos andares tem o prédio?"))
while andares>0:
	#teste para o que não deve ser impresso
	if andares==13:
		pass
	else:
		print(andares,"º")
	andares-=1