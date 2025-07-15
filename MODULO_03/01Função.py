# Função é um bloco de codigo identificado por uma um nome e pode receber uma lista de parametros #


# Exemplos

def exibir_mensagem():
# Def: fala pro python que isso é uma funçaõ
# exibir_mensagem: junto com o def fala que isso não é uma variavel e sim uma função
    print("Ola Mundo")

exibir_mensagem() #Quando eu chamo o python não identifica como uma variavel mas como uma função

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
#Nessa função eu coloquei um parametro que seria o nome, para eu chamar essa função eu precisso informar esse parametro
exibir_mensagem_2(nome = "Matheus") #Aqui eu chamei a função com parametro obrigatorio
exibir_mensagem_2("Matheus")        #Mesma coisa 

def exibir_mensagem_3(nome="Antonio"):
    print(f"Seja bem vindo {nome}!")
#Aqui podemos chamar a função sem passar nenhum parametro, porque quando colocamos = isso passar a ser opcional

exibir_mensagem_3()
exibir_mensagem_3("Matheus")
