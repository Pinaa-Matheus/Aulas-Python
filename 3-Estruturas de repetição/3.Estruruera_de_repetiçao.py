#Estrutura de repetição (For e While)
#Receber um numero do teclado e exiba os dois proximos

#O comando for é usado para percorrer um objeto iterável. Faz sentido usar quando sabemos o numero exato de vezes que vai repetir
texto = input("Informe um texto")
VOGAIS = "AEIOU"

for letra in texto:                 #Letra
    if letra.upper() in VOGAIS:     #.upper é pra transformar em maiusculo
        print(letra, end="")
else:   
    print()                         #Quebra de Linha

#Função Range, é usada para produzir uma sequencia de numeros inteiros
#Range(Começo, Final, Intervalo), Somente o final é obrigatorio

#Tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

#While é usado para repetir um bloco de codigo varias vezes. Faz sentido usar while quando não sabemos o numero exato de vezes que nosso bloco vai repetir.
opcao = -1

while opcao != 0:
    opcao = int(input(" [1] Sacar \n[2 Extrato] \n[0]Sair \n"))

if opcao == 1:
    print("Sacando....")
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Obrigado")