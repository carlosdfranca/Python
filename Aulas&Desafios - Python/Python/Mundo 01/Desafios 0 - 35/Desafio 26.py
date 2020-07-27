F = input('Digite uma frase qualquer: ')
print('A letra (a) se repete {} vezes.'.format(F.count('a')))
print('Ela aprece primeiramente na {}ª posição.'.format(F.find('a')+1))
print('A ultima letra (a) aparece na {}ª posição.'.format(F.rfind('a')+1))