## Criando Tuplas ##

frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)

## Consultar Valores ##

frutas = ("laranja", "pera", "uva",)
frutas[0]  # Maçã
frutas[2]  # Uva

## Tuplas dentro de Tuplas

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0]
matriz[0][0]
matriz[0][-1]