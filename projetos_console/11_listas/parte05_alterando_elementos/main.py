
frutas = [
    "Maçã",
    "Banana",
    "Laranja",
    "Uva",
    "Pera",
    "Abacaxi",
    "Manga",
    "Kiwi",
    "Morango",
    "Cereja",
    "Melancia"
]

# imprimindo os elementos da lista
print("\nLista de frutas:")
for fruta in frutas:
    print(fruta)

# imprimando o indice de cada elemento da lista
print("\nLista de frutas com os indices:")
for i in range(len(frutas)):
    print(f"Indice {i}: {frutas[i]}")


# alterando um elemento da lista a partir do indice informado pelo usuario
try:
    indice = int(input(f"\nDigite o indice do elemento que deseja alterar (0 a {len(frutas) - 1}): "))
    if indice < 0 or indice >= len(frutas):
        print("\nIndice invalido!")
    else:
        nova_fruta = input("\nDigite o nome da nova fruta: ").title().strip()
        # alterando o elemento da lista na posicao informada pelo usuario
        frutas[indice] = nova_fruta
        print(f"\nFruta alterada com sucesso! O elemento no indice {indice} agora é '{nova_fruta}'.")
except Exception as e:
    print(f"\nNao foi possivel alterar o elemento da lista. Erro: {e}")
finally:
    # imprimindo a lista de frutas atualizada
    print("\nLista de frutas atualizada:")
    for i in range(len(frutas)):
        print(f"Indice {i}: {frutas[i]}")