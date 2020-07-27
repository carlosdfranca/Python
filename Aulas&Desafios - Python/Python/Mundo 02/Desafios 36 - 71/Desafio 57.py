sexo = input('Informe o seu sexo:[M/F] ').strip().upper()[0]
print(sexo)
while sexo not in 'MF':
    print('Desculpe ese nãe é um valor valido, Responda novamente...')
    sexo = input('Qual é o seu sexo?[M/F] ').strip().upper()[0]
if sexo == 'M':
    print('Legal saber que você é Homem.')
else:
   print('Legal saber que você é Mulher.') 
    