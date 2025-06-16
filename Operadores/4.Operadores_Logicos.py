#São operadores utilizados em conjuntos com os operadores de comparação, para montar
#uma expressão lógica, o resultado retornado é um booleano.
saldo = 1000
saque = 200
limite = 100
conta_especial = True

saldo >= saque and saque <= limite
#Operador E, todas as partes precisam ser verdadeira, se não retorna false

saldo >= saque or saque <= limite
#Operador OU, somente uma parte precisa ser verdadeira se todos forem falso retorna false

not 1000 > 1500
#Operação de negação, Essa operação vai retornar verdadeira porque o not ele inverte as coisas.
#Nessa operação iria retornar False porem, qual é o inverso de falso verdadeiro isso que o not faz

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)
exp_2 =saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp_2)
#Parenteses