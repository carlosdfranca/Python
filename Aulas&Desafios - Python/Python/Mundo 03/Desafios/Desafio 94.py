galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Você quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Resposta não é valida, por favor digite S ou N.')
    if r in 'N':
        break
print('=-*'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média das idades cadastradas é {media:5.2f} anos')
print('As mulhers cadastradas foram ', end='')
for p in galera:
    if p['sexo']  in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('As pessoas acima da média são: ')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]} com {p["idade"]} anos.')
print('<< ENCERRADO >>')