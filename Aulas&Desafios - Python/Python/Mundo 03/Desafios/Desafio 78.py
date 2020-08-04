valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 20)
print(f'Você digitou o valor {valores}')
print(f'O maior valor foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i + 1}')
print(f'O menor valor foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i + 1}')

    