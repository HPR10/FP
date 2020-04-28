#Faça o algoritmo que leia o salario e mostre seu novo salário com 15% de aumento.
salario = float(input('Digite o valor do seu salário R$: '))
aumento = salario * 15 /100
novo_salario = salario + aumento
print('Seu salário de R${} com o novo reajuste ficou R${}'.format(salario, novo_salario))
