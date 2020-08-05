números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print(f'Adicionei {n} a lista.')
    else:
        print('Valor duplicado! Não vou adicionar')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
print('A lista em ordem crescente ficou assim:')
números.sort()
print(números)