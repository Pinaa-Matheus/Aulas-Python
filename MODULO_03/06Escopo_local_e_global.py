#O escopo refere-se à região de um programa onde uma variável ou nome é acessível e visível

salario = 2000


##Errado
#def salario_bonus(bonus):
    #salario += bonus
    #return salario

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))