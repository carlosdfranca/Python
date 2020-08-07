teste = list()
teste.append('Carlos')
teste.append('21')
galera = list()
galera.append(teste[:])#Fazer a cópia para que não se repita o "teste"
teste[0] = 'Gustavo'
teste[1] = 40
galera.append(teste[:])#Fazer a cópia para que não se repita o "teste"
print(galera)