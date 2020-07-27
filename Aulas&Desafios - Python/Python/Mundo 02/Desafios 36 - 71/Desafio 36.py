print('Lembrando que cada parcela que você desaja pagar deve corresponder a no máximo 30%  do seu salário.')
v = int(input('Qual é o valor da casa?(R$) '))
s = int(input('Me informe o valor do seu salário por favor:(R$) '))
a = int(input('Em quantos anos você pretende pagar a casa? '))
ent = int(input('Quanto você pretende dar de entrada?(R$) '))
prest = (v - ent) / (a * 12)
print('As prestações tem que ser de R${:.2f}'.format(prest))
porc = s / 100 * 30
print('30%  do seu salário é R${:.2f}'.format(porc))
if prest > porc:
    print('Desculpe, mas não podemos te realizar o empréstimo.')
    print('Tenha um bom dia.')
else:
    print('Te emprestaremos R${:.2f} mensais Até você concluir o pagamento, durante {} meses no caso.'.format(prest, a*12))
    print('É um prazer fazer negócio com você. Tenha um bom dia')
