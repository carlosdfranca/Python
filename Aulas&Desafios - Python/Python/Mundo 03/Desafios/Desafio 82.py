numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Você quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Lista completa: {numeros}')
print(f'Valores pares:{pares}')
print(f'Valores impares: {impares}')
