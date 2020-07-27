n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
	[ 1 ] Converter para BINÁRIO
	[ 2 ] Converter para OCTAL
	[ 3 ] Converter para HEXADECIMAL ''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para binário é: {}'.format(n, bin(n)))
elif op == 2:
    print('{} convertido para octal é: {}'.format(n, oct(n)))
else:
    print('{} convertido para hexadecimal é: {}'.format(n, hex(n)))
