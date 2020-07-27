n = ('Banana', 'Maça', 'Limao', 'Laranja', 'Melancia')
for c in n:
    print(f'\nNa plavra {c} temos', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
