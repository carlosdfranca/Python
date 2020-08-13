estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidae Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()