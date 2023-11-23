"""
Desenvolva um programa que recebe do usuário 
nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará 
o nome do usuário e a idade que completou, 
ou completará, no ano atual (2022).

Caso o usuário não digite um número 
ou apareça um inválido no campo do ano, 
o sistema informará o erro e continuará perguntando 
até que um valor correto seja preenchido.
"""

#verificador para teste
dadosCorreto=False

anoAtual=2022

while (dadosCorreto==False):
	#tratamento de erros
	try:
		#recebimento de dados do usupario
		nome=input("Qual seu nome?\n")
		ano=int(input("Qual ano vc nasceu?\n"))

	
		if(1922<=ano<=2021):
			idade=anoAtual-ano			
			print(nome ," ",idade)
			dadosCorreto=True
	except:
		print("Valor inválido")





