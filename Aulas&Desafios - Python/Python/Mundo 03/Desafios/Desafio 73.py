tab = ('Lakers', 'Clippers', 'Nuggets', 'Jazz', 'Thunder', 'Rockets', 'Mavericks', 'Grizzliers', 'Trail Blazers', 'Pelicans')
print('=-'*30)
print('Classificação NBA  - West Conference (TOP 10)')
print(tab)
print('=-'*30)
print(f' - 5 primeiros colocados: {tab[:5]}')
print('-'*60)
print(f' - 4 ultimos colocados: {tab[6:]}')
print('-'*60)
print(f' - Times em ordem alfabética: {sorted(tab)}')
print('-'*60)
print(f'O Lakers está em {tab.index("Lakers") + 1}º lugar')