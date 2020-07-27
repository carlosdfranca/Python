n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
r = 0
m = 0
while r != 5:
    print(' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa')
    r = int(input('O que você quer fazer com os números? '))
    if r == 1:
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, n1+n2))
    elif r == 2:
        print('O número {} multiplicado {} vezes é ugual a {}.'.format(n1, n2, n1*n2))
    elif r == 3:
        if n1 > n2:
            m = n1
        elif n2 > n1:
            m = n2
        else:
            m == 'nulo'
        print('O maior número entre os dois é {}.'.format(m))
    elif r == 4:
        print('Ok! Vamos denovo então.')
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif r == 5:
        print('Obrigado por jogar.')
    else: 
        print('Valor inválido.')

