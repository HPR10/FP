#crie um programa que leia um numero real e mostre na tela sua porção inteira.
#6.127 - 6 
from math import trunc
num = float(input('Digite um número real: '))
num_int = trunc(num)
print('A parte inteira do número {} real escolhido é {}'.format(num, num_int))




