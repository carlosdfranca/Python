# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos Alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = input('Primeiro Nome: ')
n2 = input('Segundo Nome: ')
n3 = input('Terceiro Nome: ')
n4 = input('Quarto Nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
