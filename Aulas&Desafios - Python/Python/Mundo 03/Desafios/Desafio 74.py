from random import randint
n = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100), )
print(f'Os valores sorteados foram: ')
for c in n:
    print(f'{c}', end=' ')
print(f'\nO maior valor foi o {max(n)}')
print(f'O menor valor foi o {min(n)}')
