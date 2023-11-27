"""
	A loja de cosméticos ficou muito feliz com
	 seu trabalho e chamaram você novamente!
	  Dessa vez, eles precisam que você atualize 
	  o array de produtos. Agora, eles estão vendendo 
	  rímel ao invés de batons, e cremes hidratantes 
	  no lugar de loções. Além disso, ficaram sem
	   delineadores, então precisam que você remova ele 
	   da lista de produtos. Imprima a nova lista no 
	   terminal para verificar que as alterações foram 
	   realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

Como desafio, adicione dois novos produtos da sua escolha à lista. 
"""
#lista base
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

print(lista_produtos)

#substituição de rímel ao invés de batons
del lista_produtos[1]
lista_produtos.insert(1,'rímel')

#substituição de e cremes hidratantes no lugar de loções
del lista_produtos[4]
lista_produtos.insert(4,'cremes hidratantes')

#remoção de deliniadores
del lista_produtos[7]
print(lista_produtos)

lista_produtos.append("fone de ouvido")
lista_produtos.append("pelúcia de gato")
lista_produtos.append("perfume")

print(lista_produtos)