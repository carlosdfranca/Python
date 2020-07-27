n = cont = 0
while True:
    n = int(input('Você quer ver a tabuada de qual número?'))
    if n < 0:
        break
    print('-' * 30)
    for cont in range(1, 11):
        print(f'{n} x {cont:2} = {n * cont}')
    print('-' * 30)
print('Não fazemos tabuadas com números negativos.')
    