"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

"""

#Leitura dos números a serem trabalhados
n1=float(input("Informe o primeiro número"))
n2=float(input("Informe o segundo número"))

#definição da operação matemática a ser realziada
print("1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão")
operacao=int(input("Qual operação deseja realizar"))

#testes para saber se é operação válida ou realiza a operação
if 0<operacao<5: 
	if operacao==1:
		print(n1+n2)
	elif operacao==2:
		print(n1-n2)
	elif operacao==3:
		print(n1*n2)
	elif operacao==4:
		print(n1/n2)

else:
	print(0)
