from random import choice
n1 = input('Primeiro Nome: ')
n2 = input('Segundo Nome: ')
n3 = input('Terceiro Nome: ')
n4 = input('Quarto Nome: ')
lista = [n1, n2 , n3 , n4]
escolhido = choice(lista)
print ('O aluno escolhido foi {}'.format(escolhido))
