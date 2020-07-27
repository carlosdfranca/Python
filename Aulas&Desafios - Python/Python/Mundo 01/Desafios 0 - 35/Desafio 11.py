print('========Desafio 11========')
print('Precisa calcular o quanto de tinta precisa para pintar sua parede? \n \n Seus Problemas acabaram! \n \n Me diga:')
l = float(input('Quanto mede a largura da parede(m): '))
a = float(input('Quanto mede a altura da parede(m): '))
a2 = l*a
t =  a2/2 
print('A parede possui {}m², assim você precisara de {}l de tinha para pintá-la'.format(a2, t))