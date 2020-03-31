#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.
met = int(input('Digite um valor em metros: '))
centi = met * 100
mil = met * 1000
km = met / 1000

print('O valor em metros é {}m² em centimetros fica {}cm em milimetros {}mm e Quilometros {}km'.format(met, centi, mil, km))

