num = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print('=-' * 30)
#print(f'Todos os valores: {num}')
num[0].sort()
num[1].sort()
print(f'Números pares: {num[0]}')
print(f'Números impares: {num[1]}')
