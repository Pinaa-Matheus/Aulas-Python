#Interpolação de String

#NÃO RECOMENDADO - COM %

nome = "Guilerme"
idade = 18
profissao = "Estagiario"
linguagem = "Python" 

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem)) #No final é a ordem das variaveis que vão aparecer
#%s -> String
#%d -> Inteiro(decimal)

#ELA NÃO É USADA PELO FATO QUE É MUITO COMPLEXO E QUANDO VOCE TRABALHA COM MUITAS VARIAVEIS FICA MUITO COMPLEXO DE TRABALHAR


#METODO FORMAT
nome = "Guilerme"
idade = 18
profissao = "Estagiario"
linguagem = "Python" 

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {0}".format(linguagem, idade, profissao, nome)) #Lembrando 0 é numero

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {prof} e estou matriculado no curso de {ling}".format(nome=nome, idade=idade, prof=profissao, ling=linguagem))


#F-STRING

nome = "Guilerme"
idade = 18
profissao = "Estagiario"
linguagem = "Python" 

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")


#FORMATAÇÃO COM F-STRING
PI = 3.1415926535

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}") #{PI:(numero de espaços).(numero de casas)f}