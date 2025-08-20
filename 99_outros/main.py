usuarios = [
    {
        "nome": "Calebe Campos",
        "idade": 30,
        "profissao": "Desenvolvedor Python",
        "data_nascimento": "1993-05-15"
    },
    {
        "nome": "Maria Silva",
        "idade": 25,
        "profissao": "Analista de Sistemas",
        "data_nascimento": "1998-08-20"
    },
    {
        "nome": "Carlos Souza",
        "idade": 28,
        "profissao": "Designer Gráfico",
        "data_nascimento": "1995-02-10"
    }
]

# exibindo apenas uma chave especifica de cada dicionario da lista, usando apenas um for
for usuario in usuarios:
    print(f"Nome: {usuario.get('nome')}")
print("\n")

# exibindo apenas uma chave especifica de cada dicionario da lista, usando um for dentro de outro
for usuario in usuarios:
    for chave, valor in usuario.items():
        if chave == "nome":
            print(f"{chave.capitalize()}: {valor}")
print("\n")

# exibindo apenas uma chave especifica de cada dicionario da lista, usando apenas o print
[print(f"profissao: {usuario['profissao']}") for usuario in usuarios]

# exibindo apenas uma chave especifica de cada dicionario da lista, usando map() com funcao lambda
list(map(lambda u: print(f"profissao: {u['profissao']}"), usuarios))




# exibindo apenas chaves especificas de cada dicionario da lista
for usuario in usuarios:
    print(f"Nome: {usuario.get('nome')}")
    print(f"Profissao: {usuario.get('profissao')}")
    print('-'*40)
print("\n")

# exibindo apenas chaves especificas de cada dicionario da lista
for usuario in usuarios:
    for chave, valor in usuario.items():
        if chave in ("nome","profissao"):
            print(f"{chave.capitalize()}: {valor}")
    print('-'*40)
print("\n")

