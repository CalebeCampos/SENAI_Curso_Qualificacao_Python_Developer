nomes = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve"
]

# imprimindo a lista original
print("\nLista original:")
for nome in nomes:
    print(nome)


# adicionando um novo nome à lista
nomes.append("Frank")
print("\nLista apos inserir um novo elemento ao final da lista:")
for nome in nomes:
    print(nome)


# adicionando um novo nome na posição 2
nomes.insert(2, "Grace")
print("\nLista apos insirir um novo elemento exatamente no indice 2:")
for nome in nomes:
    print(nome)


# adicionando um novo nome informado pelo usuario na lista
novo_nome = input("\nDigite um novo nome para adicionar à lista: ").title().strip()
nomes.append(novo_nome)
print("\nLista apos inserir um novo elemento no final informado pelo usuario:")
for nome in nomes:
    print(nome)