r = 's'
media = maior = cont = soma = menor = 0
while r == 's':
    cont += 1
    n = int(input('Didite um número: '))
    soma = soma + n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    r = str(input('Quer continuar [S/N]? ').lower())
print('=-' * 20)
print('Você digitou {} números.'.format(cont))
print('A média entre os números digitados é {}'.format(media))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
print('=-' * 20)    
