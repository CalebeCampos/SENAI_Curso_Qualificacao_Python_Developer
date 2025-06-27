pessoa = {
    'nome': "João",
    'idade': 30,
    'email': "joao@example.com",
    'profissao': "Engenheiro"
}

# exibindo o valor de cada chave usando o laço for e o método get()
for chave in pessoa:
    print(f"{chave.capitalize()}: {pessoa.get(chave)}")

print("\n")

# exibindo o valor de cada chave usando o laço for e o método items()
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")
