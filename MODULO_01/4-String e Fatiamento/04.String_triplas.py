nome = "Matheus"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
    Essa mensagem tem diferentes recuos.
"""
print(mensagem)

mensg = """
Ola meu nome é {nome},
Eu estou aprendendo Python
""".format(nome=nome)
print(mensg)


#ISSO É BOM PARA FAZER MENUS 