n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite um último número: ')))
print(f'Você digitou os valores: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O primeiro número 3 foi colocado na {n.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi colocado em nenhuma posição')
print(f'valores pares digitados: ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c}', end=' ')
