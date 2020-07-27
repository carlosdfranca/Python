from random import randint
pi = result = ''
pc = p = soma = w = 0
while True:
    pi = str(input('Par ou Impar? ')).lower()
    pc = int(randint(0, 10))
    p = int(input('O computador ja pensou num número. Qual númeor vc escolhe para jogar? '))
    soma = pc + p
    if soma % 2 == 0:
        result = 'par'
    else:
        result = 'impar'
    if pi == 'par' and result == 'par' or pi == 'impar' and result == 'impar':
        w += 1
        print('-' * 30 )
        print (f'''VocÊ ganhou!!! 
O computador escolheu {pc} e você escolheu {p}. Total de {soma} deu {result}
Continue jogando para acomular vitórias.''')
        print(f'Acumulo de Vitórias: {w}')
        print('-' * 30)
    else:
        break
print('-' * 30 )
print(f'''Você perdeu... 
O computador escolheu {pc} e você escolheu {p}. Total de {soma} deu {result}.
Acumulo de vitórias: {w}''')
print('-' * 30 )
