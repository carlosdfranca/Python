print('ESTRUTURAS DE CONTROLE')
print('==Condições Aninhadas==')
nome = input('Qual é o seu nome? ')
if nome == 'Carlos' or nome == 'Rwency':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Gustavo' or nome == 'Gabriel':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normalzinho.')
print('Tenha um bom dia, {}.'.format(nome))
