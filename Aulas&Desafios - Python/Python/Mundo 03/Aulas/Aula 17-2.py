valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
for c, v in enumerate(valores):
    print(f'Na {c + 1}ª posição, encontrei o valor {v}.')
print('Cheguei ao final da lista.')