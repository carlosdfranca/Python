print('TIPOS DE TRIÂNGULO')
A = int(input('Lado A do triângulo: '))
B = int(input('Lado B do triângulo: '))
C = int(input('Lado C do triângulo: '))
if A == B and B == C:
	print('Você tem um triângulo equilátero')
elif A != B and B != C and C != A:
	print('Você tem um triângulo Escaleno')
elif A == B or B == C or C == A:
	print('Você tem um triângulo Isósceles') 