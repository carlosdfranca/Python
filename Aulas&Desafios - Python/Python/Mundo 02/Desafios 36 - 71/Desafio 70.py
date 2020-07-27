produto = nmb = ''
preço = soma = mb = mm = cont = 0
while True:
    print('-'*30)
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço do preoduto: R$'))
    cont += 1
    soma += preço
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('-'*30)
    if preço > 1000:
        mm += 1
    if cont == 1:
        mb = preço
        nmb = produto
    else:
        if preço < mb:
            mb = preço
            nmb = produto
    if r == 'N':
        break
print('=-'*20)
print(f'Total de gasto da compra: R${soma:.2f}')
print(f'Produtos que custam mais de R$1000,00: {mm}')
print(f'Produto mais barato: {nmb}')
print('=-'*20)