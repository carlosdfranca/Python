print('=============================')
print('		10 TERMOS DE UMA PA		')
print('=============================')
i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
termo = i 
cont = 1
while cont < 11:
    print('{} >>> '.format(termo), end='')
    termo += p
    cont += 1
print('FIM')