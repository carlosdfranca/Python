print('=============================')
print('		10 TERMOS DE UMA PA		')
print('=============================')
i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
termo = i 
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} >>> '.format(termo), end='')
        termo += p
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Você mostrou no total {} termos.'.format(total))
print('FIM')