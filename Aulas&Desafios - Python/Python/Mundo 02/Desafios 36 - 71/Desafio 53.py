frase = str(input('Digte a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
	inverso += junto[letra]
if inverso == junto:
	print('Temos um palíndromo')
else:
	print('A frase não é um palíndromo')

