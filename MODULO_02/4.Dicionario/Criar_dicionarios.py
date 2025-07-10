#Dicionario é um conjunto não-ordenado de pares chave:valor, onde as chaves são unicas

## Declarar um dicionario

pessoa = {"nome": "Guilermer", "idade": 28}

#Outra forma é usando o dict

pessoa = dict(nome= "Guilerme", idade=28)

#Nessa forma é quando temos um dicionario ja criado e queremos adicionar uma nova chave 

pessoa["telefone"] = "3333-1234"
print(pessoa)