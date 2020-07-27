name = input('Digite seu nome completo: ')
div = name.split()
print('Primeiro nome: {}'.format(div[0]))
print('Último nome: {}'.format(div[len(div)-1]))