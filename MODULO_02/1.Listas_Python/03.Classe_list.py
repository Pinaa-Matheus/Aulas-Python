## [].append - Para adicionar alguma coisa ##

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

## [].clear - Limpar minha lista

print(lista)

lista.clear #Limpou a lista

print(lista)

## [].copy - Copiar uma lista

lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista2, lista2)

## [].count - Contar quantas vezes determinado objeto aparece na sua lista
cores = ["vermelho", "vermelho", "azul", "verde"]

print(cores.count("vermelho"))
print(cores.count("azul"))

## [].extende - Juntar listas

linguagens = ["python", "js", "c"]
print(linguagens)
linguagens.extend(["java", "csharp"])
print(linguagens)

## [].index - Posição do objeto
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.index("java")   # 3
linguagens.index("python") # 0

## [].pop - Ele tira o ultimo elemento da lista
linguagens = ['python', 'js', 'c', 'java', 'csharp'] 
linguagens.pop()  #csharp
linguagens.pop()  #java
linguagens.pop(0) #python
print(f"Lista com o pop{linguagens}")

## [].remove - Ele tira elementos da lista
linguagens = ['python', 'js', 'c', 'java', 'csharp', "c"] 

linguagens.remove("c") 

#Porem ele remove a primeira ocorrencia daquilo que vc quer ele não remove todos 

print(linguagens)

## [].remove - Inverte a lista
linguagens = ['python', 'js', 'c', 'java', 'csharp'] 
linguagens.reverse()
print(linguagens)

## [].sort - Ordena a lista

linguagens = ['python', 'js', 'c', 'java', 'csharp'] 
linguagens.sort() #Ordem alfabetica
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp'] 
linguagens.sort(reverse=True) #ordem alfabetica porem invertido

## len - Quantidade da elementos da lista
len(linguagens)