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


# imprimando o indice de cada elemento da lista
print("\nLista de frutas com os indices:")
for i in range(len(frutas)):
    print(f"Indice {i}: {frutas[i]}")

try:
    indice = int(input(f"\nDigite o indice do elemento que deseja alterar (0 a {len(frutas) - 1}): "))
    if indice < 0 or indice >= len(frutas):
        print("\nIndice invalido!")
    else:
        # removendo o elemento da lista na posicao informada pelo usuario
        del(frutas[indice])
        print("\nFruta removida com sucesso!")
except Exception as e:
    print(f"\nNao foi possivel remover o elemento da lista. Erro: {e}")
finally:
    # imprimando o indice de cada elemento da lista
    print("\nLista de frutas apos remocao do elemento:")
    for i in range(len(frutas)):
        print(f"Indice {i}: {frutas[i]}")