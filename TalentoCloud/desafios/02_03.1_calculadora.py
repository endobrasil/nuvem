"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.


"""

#definição da função calculadora
def calculadora():
	#A opção a ser escolhida pelo usuário
	opcao=1;

	while(opcao!=0) : #enquanto ele não escolher para sair...
		#definição da operação matemática a ser realziada
		print("1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n 0. Para sair\n")
		try:
			opcao=int(input("Qual operação deseja realizar\n"))
			if(opcao!=0): #se escolher zero ele finaliza a aplicação
				#Leitura dos números a serem trabalhados
				n1=float(input("Informe o primeiro número\n"))
				n2=float(input("Informe o segundo número\n"))

				if 0<opcao<5: 
					if opcao==1:
						print("resultado: ",(n1+n2))
					elif opcao==2:
						print("resultado: ",(n1-n2))
					elif opcao==3:
						print("resultado: ",(n1*n2))
					elif opcao==4:
						if(n2==0):
							print("O dividendo não pode ser zero\n")
						else:
							print("resultado: ",(n1/n2))
					else:
						print("Opção invalida\n")


		except:
			print("Valor inválido\n")

calculadora()