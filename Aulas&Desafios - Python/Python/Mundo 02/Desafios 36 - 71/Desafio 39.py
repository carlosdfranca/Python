ano = int(input('Em que ano você nasceu? '))
idade = 2020 - ano
if idade < 18:
    print('Faltam {} para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Já está na hora de se alistar')
else:
    print('Já passou uns {} anos desde de que você precisava se alistar né mermão? tu ta é fodido.'.format(idade - 18))
