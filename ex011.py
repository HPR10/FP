#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá
#Sabendo que cada litro de tinta, pinta uma área de 2m² 
larg = float(input('Qual a altura da sua parede: '))
alt = float(input('Qual a largura da sua parede: '))
area = larg * alt 
print('Sua parede tem a dimensão de {} x {} e sua área é {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede será necessario {:.0f}litros de tinta!'.format(tinta))



