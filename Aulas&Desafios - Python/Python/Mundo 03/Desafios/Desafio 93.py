dados = {}
partidas = []
dados['Jogador'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
for c in range(1, tot+1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)
print('=-'*30)
for k, v in dados.items():
    print(f'{k}: {v}')
print('=-'*30)
print(f'O jogador {dados["Jogador"]} jogou {len(dados["Gols"])} partidas')
for i, v in enumerate(dados['Gols']):
    print(f'    => Na partida {i+1}, fez {v} gol(s).')
print(f'Foi um total de {dados["Total"]} gols')



