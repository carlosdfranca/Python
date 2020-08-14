time = []
dados = {}
partidas = []

while True:
    dados.clear()
    partidas.clear()
    dados['Jogador'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
    for c in range(1, tot+1):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dados['Gols'] = partidas[:]
    dados['Total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if r == 'N':
        break
print('-=*'*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Jogador"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')