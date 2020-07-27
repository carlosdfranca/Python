n = cont = s = 0
while True:
    n = int(input('Digite um número: [999 faz parar]'))
    if n == 999:
        break
    cont += 1
    s += n 
print(f'Você digitou {cont} números')
print(f'A soma entre os números vale {s}.') 