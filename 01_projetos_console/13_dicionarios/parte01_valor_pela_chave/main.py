usuario = {
    'nome': "João",
    'idade': 30,
    'email': "joao@example.com",
    'profissao': "Engenheiro"
}

# exibindo o tipo da variável usuario
print(type(usuario))

# exibindo o dicionário
print(usuario)

# exibindo os valores do dicionário
print(usuario.values())

# exibindo as chaves do dicionário
print(usuario.keys())

# exibindo os itens do dicionário
print(usuario.items())

# exibindo o valor de cada chave
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"E-mail: {usuario['email']}")
print(f"Profissão: {usuario['profissao']}")
