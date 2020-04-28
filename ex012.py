#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input("Qual o valor do produto selecionado R$: "))
preco_c = preco * 0.05
preco_f = preco - preco_c
print('O preço do produto com desconto é {}R$'.format(preco_f))




