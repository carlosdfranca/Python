dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
print(f'Nome: {dados["nome"]}')
print(f'Média: {dados["média"]}')
if dados['média'] >= 7:
    dados['Situação'] = 'Aprovado'
elif 5 <= dados['média'] < 7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'
print(F'Situação: {dados["Situação"]}')