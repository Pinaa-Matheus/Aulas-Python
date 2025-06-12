age = int(23)
name = "Matheus"
print(f"Meu nome é {name} e eu tenho {age} anos de idade")


age, name = (23, "Matheus")     #Da pra declarar varias variaveis em uma linha
print(f"Meu nome é {name} e eu tenho {age} anos de idade")   

age = 1.5   #Posso transformar int para float, e quando eu coloco um numero quebrado
print(age)  #como int ele aredonda 

##CONSTANTES

DEBUG = True                        #Em Python, não existe um mecanismo nativo para definir constantes
STATES = ["SP", "RJ", "MG"]         #Com isso os programadores tem um "lei" que toda constante é escrita em maiúsculo
AMOUNT = 30.2
