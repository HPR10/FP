#leia um angulo e mostre na tela o valor do seno, cosseno e tangente desse angulo.
from math import sin, cos, tan, radians
ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cose = cos(radians(ang))
print('O angulo de {} tem o COSENO de {:.2f}'.format(ang, cose))
tang = tan(radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tang))
