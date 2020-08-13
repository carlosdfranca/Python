pessoas = {'nome' : 'Carlos', 
           'idade' : 22, 
           'sexo' : 'Masculino'
}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys()) #Mostra as chaves(nome, idade e sexo).
print(pessoas.values()) #Mostra os valores.
print(pessoas.items()) #Mostra todos os itens.
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
pessoas['nome'] = 'Leandro' #Sbstituiu o valor dentro da chave "nome"
pessoas['peso'] = 98.5 #Pode adicionar uma chave sem precisa do append
del pessoas['sexo'] #pode deletar itens ou valores
for k, v in pessoas.items():
    print(f'{k} = {v}')
