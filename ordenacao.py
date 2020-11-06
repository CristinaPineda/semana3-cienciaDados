# ordenação 

'''
Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente
'''

a = int(input('digite um número: '))
b = int(input('digite um número: '))
c = int(input('digite um número: '))

if a < b < c:
	print('crescente')
else:
	print('não está em ordem crescente')