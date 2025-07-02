## COMO CRIAR LISTAS ##

#Lista em Python podem armazenar de maneira sequencial qualquer tipo de objeto.

frutas = ["laranja", "maca", "uva"] #Forma mais comum
frutas = []                         #Posso criar listas vazias tambem

letras = list("python")
print(letras)

carro = ["Ferrari", "F8", 420000, 2020, 2900 , "São Paulo", "True"]

## COMO ACESSAR OS VALORES ##

#A lista é uma sequencia, portanto podemos acessar seus dados utilizando indices
frutas = ["laranja", "maca", "uva"]
frutas[0]   #laranja
frutas[2]   #uva

# Valores Negativos #

frutas = ["maçã", "laranja", "uva", "pera"]
frutas[-1]  #pera
frutas[-3]  #laranja
#     (-1)       (0)         (1)
#     Pera       Maçã      Laranja
 

## MATRIZ ##

matriz = [
    [1, "a",  2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0]           #[1, "a",  2]
matriz[0][0]        # 1
#Basicamente é linha é coluna 

## FATIAMENTO ##

lista = ["p", "y", "t", "h", "o", "n"]
lista[2:]            #["t", "h", "o", "n"]
lista[:2]            #["p", "y"]
lista[1:3]           #["y", "t"]
lista[0:3:2]         # ["p", "t"]
lista[::-1]          # ["n", "o", "h", "t", "y", "p"]
                     #lista[início:fim:passo]


## ALTERAR LISTAS ##

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carros)

#Precisamos, criar uma variavel temporaria para representar cada item da lista durante a repetição 


## FILTRO VERSAO ##
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) #O .append é para adicionar uma variavel na lista 

#Outra forma
# pares [numero for numero in numeros if numero % == 0]

## MODIFICANDO VALORES VERSÃO ##
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]