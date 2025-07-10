# Criando um dicionário de exemplo
meu_dict = {'nome': 'Matheus', 'idade': 18, 'cidade': 'São Paulo'}

# 1. get(): retorna o valor de uma chave. Se não existir, retorna None ou valor padrão.
print("get:", meu_dict.get('nome'))  # Existe
print("get com valor padrão:", meu_dict.get('altura', 'Não informado'))  # Não existe

# 2. keys(): retorna uma visão com todas as chaves
print("keys:", list(meu_dict.keys()))

# 3. values(): retorna uma visão com todos os valores
print("values:", list(meu_dict.values()))

# 4. items(): retorna pares (chave, valor)
print("items:", list(meu_dict.items()))

# 5. update(): atualiza o dicionário com outro dicionário ou pares chave-valor
meu_dict.update({'idade': 19, 'altura': 1.75})
print("update:", meu_dict)

# 6. pop(): remove uma chave e retorna seu valor
idade = meu_dict.pop('idade')
print("pop (idade):", idade)
print("dicionário após pop:", meu_dict)

# 7. popitem(): remove e retorna o último item inserido (Python 3.7+)
ultimo_item = meu_dict.popitem()
print("popitem:", ultimo_item)
print("dicionário após popitem:", meu_dict)

# 8. setdefault(): retorna o valor da chave, e se não existir, insere com valor padrão
print("setdefault existente:", meu_dict.setdefault('nome', 'Outro'))
print("setdefault nova chave:", meu_dict.setdefault('pais', 'Brasil'))
print("dicionário após setdefault:", meu_dict)

# 9. clear(): remove todos os itens
copia = meu_dict.copy()  # Para mostrar depois
meu_dict.clear()
print("clear:", meu_dict)

# 10. copy(): retorna uma cópia superficial do dicionário
print("copy:", copia)

# 11. fromkeys(): cria um novo dicionário com chaves dadas e um valor padrão
chaves = ['a', 'b', 'c']
novo_dict = dict.fromkeys(chaves, 0)
print("fromkeys:", novo_dict)

# 12. in: verifica se uma chave está no dicionário (não é método, mas é útil!)
print("'nome' in copia:", 'nome' in copia)

# 13. del: remove um item pela chave (também não é método, mas é muito usado)
del copia['nome']
print("del 'nome':", copia)

# Fim da demonstração
print("Todos os métodos principais da classe dict foram mostrados.")
