lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1 
    r = str(input('Você quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('==' * 30)
print(f'Foram digitados {len(lista)} valores.')
print('=-' * 20)
lista.sort(reverse=True)
print(f'Lista em ordem decrescente {lista}.')
print('=-' * 20)
if 5 in lista:
    print(f'Foi encontrado o valor 5 na lista.')
else:
    print('Não encontrei o valor 5 na lista.')