#Leia o comprimento do cateto oposto e do cateto adjacente de um triangulo relatngulo, calcule
# e mostre o comprimento da hipotenusa.
import math
co = float(input('Qual o valor da cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))



#Valor da hipotenusa (co ** 2 + ca ** 2) ** (1/2) - Raiz quadrada. 
