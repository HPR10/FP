#Calculo do valor de aluguel de um carro.
dias = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros rodados? '))
valor_dias = dias * 60
valor_km = km * 0.15
valor_total = valor_km + valor_dias
print('O total a pagar é de R${:.2f}'.format(valor_total))
