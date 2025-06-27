
# criando um dicionário com informações de uma pessoa utilizando o método dict()
usuario = dict(
    nome="João",
    idade=30,
    email="joao@example.com",
    profissao="Engenheiro"
)

# exibindo o tipo da variável usuario
print(type(usuario))

# exibindo as chaves e valores do dicionário usando o laço for e método get()
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")