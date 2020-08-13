from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc 
dados['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['Carteira'] != 0:
   dados['Ano de contratação'] = int(input('Ano de contratação: '))
   dados['Aposentadoria'] = dados['Idade'] + (35 - (datetime.now().year - dados['Ano de contratação']))
   dados['Salário'] = float(input('Salário: R$'))
for k, v in dados.items():
    print(f'{k}: {v}')