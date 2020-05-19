#Um professor quer sortear um dos seus quatros alunos para apaga o quadro. faça um programa 
#que ajude ele, lendo os nomes deles e escrevendo o nome do escolhido.
import random 
nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
sorteio = [nome1, nome2, nome3, nome4]
sorteado = random.choice(sorteio)
print('O aluno sorteado é {}'.format(sorteado))
