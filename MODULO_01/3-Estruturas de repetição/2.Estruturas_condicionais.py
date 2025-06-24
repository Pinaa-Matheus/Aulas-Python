###############SO FAZENDO COM O IF################
#saldo = 2000
#saque = float(input("Informe o valor do saque: "))

#if saldo >= saque:
    #print("Realizando o saque!")

#if saldo < saque:
    #print("Saldo insuficiente!")
##################################################
import sys


saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente")
#######################################################
opcao = int(input("Informe uma opção: [1] sacar \n[2] Extrato: "))
if opcao == 1:
    valor = float(input("Informe a quantidade para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato ....")
else:
    sys.exit("Opção inválida")
##########################################
#Tambem podemos ter if dentro de if
conta_normal = True
conta_universitaria = False
cheque_especial = 1000


if conta_normal: #Exemplo sistema de banco
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
#######################################
#If em uma linha, isso pode ser util em operaçoes simples
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")

#Se saldo for maior que o saque ele vai retornar Sucesso se não ele retorna Falha