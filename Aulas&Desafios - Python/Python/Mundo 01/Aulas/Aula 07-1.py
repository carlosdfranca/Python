n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2 
m = n1 * n2
d = n1 / n2
dInt = n1 // n2 
p = n1 ** n2 
r = n1 % n2 
print('A soma vale {}, a subtração vale {}, a multiplicação vale {}, a divisão vale {:.3f}'.format(s,sub,m,d), end=' ')
print('a potencia vale {} e o resto da divisão vale {}'.format(p,r))