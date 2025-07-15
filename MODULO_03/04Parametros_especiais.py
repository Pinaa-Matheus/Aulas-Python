
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

    #Post1 e post2 são posicionais 
    #   / indica que todos os parâmetros antes dele devem ser passados apenas por posição
    #pos_or_kwd são possicionais ou palavras-chaves
    #   * indica que todos os parâmetros depois dele devem ser passados apenas com nome
    #kwd1 e kwd2 são palavras-chaves


def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 2002, "ABC-1111", "Fiat", motor=1.4, combustivel="flex")
# Invalido criar_carro(modelo="Fox", ano=2001, placa="ABC-1112", marca="Vw", motor="1.0", combustivel="Flex")

def criar_carro2(*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo="Gol", ano=2014, placa="ABC-1234", marca="Vw", motor=1.0,  combustivel="Gas")