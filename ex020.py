#Faça um programa que sorteie a ordem de apresentação de trabalhos dos alunos.
#leia o nome de quatros alunos e mostre a ordem sorteada.
import random
nome1 = str(input('Primeiro nome: '))
nome2 = str(input('Segundo nome: '))
nome3 = str(input('Terceiro nome: '))
nome4 = str(input('Quarto nome: '))
sorteio = [nome1, nome2, nome3, nome4]
random.shuffle(sorteio)
print('A ordem da apresentação é {}'.format(sorteio))


