#Conjunto ele é coleção que não possui objetos repetidos

teste = set([1, 2, 3, 4, 3 , 4])
print(teste)

teste02 = set("abacaxi")    #Quando vc usa set, não confie na ordem dele.
print(teste02)
#Nesse exemplo que usamos ele vai mostrar de varias formas diferentes


## Acessando os dados ##
#conjuntos em Python não suportam indexação e nem fatiamento, casa queira acessar é necessarios converter. 

numeros = {1, 2, 3, 2}
##print(numeros[0])

numeros = list(numeros)
print(numeros[0])



## Metodos com o set ##

#Union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)

#Intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b)

#Difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

#symmetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b)

#issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) #False 
conjunto_b.issubset(conjunto_a) #True

#isdisjoint
conjunto_a = {1, 2, 3}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False


#add
sorteio = {1, 23}

sorteio.add(25)
print(sorteio)
sorteio.add(45)
print(sorteio)
sorteio.add(25)
print(sorteio)

#clear

sorteio.clear() #Limpa

#copy
sorteio = {1, 23}
sorteio.copy

