idade = ma18 = me20 = homens = 0
while True:
    print('-'*30)
    nome = ' '
    nome = str(input('Qual o nome? '))
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]? ')).strip().upper()[0]
    print('-'*30)
    if idade > 18:
        ma18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        me20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('=-'*20)
print('Nos dados que você preencheu tem:')
print(f'- Pessoas com mais de 18 anos: {ma18}')
print(f'- Homens: {homens}.')
print(f'- Mulheres com menos de 20 anos: {me20}.')
print('=-'*20)