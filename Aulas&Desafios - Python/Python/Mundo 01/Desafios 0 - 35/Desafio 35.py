print('Calculo das retas que podem formar um triângulo.')
a = int(input('Comprimento da primeira reta: '))
b = int(input('Comprimento da primeira reta: '))
c = int(input('Comprimento da primeira reta: '))
if a < b+c and b < a+c and c < a+b:
    print('Você tem um triângul equilatero.')
else:
    print('Você NÃO tem um triângul equilatero.')
print('--FIM--')