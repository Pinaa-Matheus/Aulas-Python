#Operadores de identidade são usados para verificar se duas variáveis referenciam o mesmo objeto na memória
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
#Ela vai retornar True pelo fato que nome_curso recebe curso

curso is not nome_curso
#Retorna True se as duas variáveis apontam para objetos diferentes 