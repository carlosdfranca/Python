import random
r = 0
n = 1
print('O computador pensou num número de 0 à 5.')
while n != r:
    n = int(random.randint(0 , 5))
    r = int(input('Qual número você acha que é? '))
    if r == n:
        print('Parabéns, o número que o computador pensou era {} . você é bom de chute!!'.format(n))
    else:
        print('Foi mal, não foi dessa vez. O computador pensou em {} .'.format(n))
print('--FIM--')
