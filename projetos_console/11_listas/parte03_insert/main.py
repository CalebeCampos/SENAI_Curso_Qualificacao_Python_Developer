cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']

# imprimindo o tamanho da lista
print(f"\nTamanho da lista de cidades: {len(cidades)}")

# imprimindo o indice de cada elemento da lista com usando o laço for
print("\nLista de cidades com os indices:")
for i in range(len(cidades)):
    print(f"Indice {i}: {cidades[i]}")


# inserindo um novo elemento na lista informado pelo usuario na posicao tambem informada pelo usuario
try:
    indice = int(input(f"\nDigite o indice onde deseja inserir uma nova cidade (0 a {len(cidades)}): "))
    nova_cidade = input("\nDigite o nome da nova cidade: ").title().strip()

    if indice < 0 or indice > len(cidades):
        print("\nIndice invalido!")
    else:
        # inserindo um novo elemento na lista na posicao informada pelo usuario
        cidades.insert(indice, nova_cidade)
        print(f"\nNova cidade '{nova_cidade}' inserida no indice {indice} com sucesso!")
except Exception as e:
    print(f"\n Nao foi possivel inserir o novo elemento na lista. Erro: {e}")
finally:
    # imprimindo o indice de cada elemento da lista com usando o laço for
    print("\nLista de cidades:")
    for i in range(len(cidades)):
        print(f"Indice {i}: {cidades[i]}")