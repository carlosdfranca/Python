matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sompar = 0
somter = 0
mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            sompar += matriz[l][c]
        if c == 2:
            somter += matriz[l][c]
        if l == 1:
            if matriz[l][c] > mai:
                mai = matriz[l][c]
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A- A soma dos pares é {sompar}')
print(f'B- A soma dos valores da terceira coluna é: {somter}')
print(f'C- O maior valor d segunda linha é: {mai}')