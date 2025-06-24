curso =  "pYtHon"
print("\nTransformações de letras \n")
print(curso.upper())#Maiusculo

print(curso.lower())#Minusculo

print(curso.title())#A primeira letra maiuscula


print("\nEspaços \n")
curso01 = "    Python "

print(curso01.strip()) #Remove todos os espaços

print(curso01.lstrip()) #Remover o espaço somente da esquerda, lstrip = left strip

print(curso01.rstrip()) #Remover o espaço somente da direita, lstrip = right strip

print("\nJunções e centralização \n")

curso02 = "Python"
print(curso02.center(10, "#")) #string.center(largura, 'SIMBOLO'), o segundo documento ele é opcional se voce não colocar nada ele so vai colocar espaços em branco

print(".".join(curso02)) #O join ele é muito utilizado para CPF

print("\nJuntar métodos  \n")

string = "   pYtHon   "
print(string.strip().lower().title())
print(".".join(string.strip()).center(20, "-"))