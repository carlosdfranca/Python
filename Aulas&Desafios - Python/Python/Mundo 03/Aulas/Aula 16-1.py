lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
#print(lanche[1:3])
#print(lanche[2:])
#print(lanche[:3])
#print(lanche[-3:])
print('=-'*20)
for cont in range(0, len(lanche)):
    print(f'Hoje vou comer {lanche[cont]} na posição {cont}.')
print('=-'*20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('=-'*20)
#Usar o exemplo acima caso for mostrar a posição.

for c in lanche:
   print(f'Eu vou comer {c}')
print('=-'*20)
#Usar esse caso não precise da posição.
print('Comi pra caramba')