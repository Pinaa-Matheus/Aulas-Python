#Toda função de python retorna None por padrão. Diferente

def calcular_total(numeros):
    return sum(numeros)
#Sum(), calcular a soma dos elementos de um iterável, como listas ou tuplas


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([1, 2, 10])


retorna_antecessor_e_sucessor(10)
#Nesse caso ele vai retornar uma tupla(imutavel)