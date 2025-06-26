import os

nomes = [
    "João",
    "Maria",
    "José",
    "Ana",
    "Pedro",
    "Lucas",
    "Carla"
]

for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}")
print('-'*60)

try:

    indice = int(input("Digite o índice do nome que deseja acessar: "))

    if indice >= 0 and indice < len(nomes):
        nome_isolado = nomes.pop(indice)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{nome_isolado} foi removido da lista.")

        # exibe os valores sem o item isolado
        for indice in range(len(nomes)):
            print(f"Índice {indice}: {nomes[indice]}")
        print('-'*60)

        # exibe o item isolado
        print(f"Item isolado: {nome_isolado}")
        print('-'*60)

    else:
        print("Índice inválido. Por favor, digite um número entre 0 e", len(nomes) - 1)

except Exception as e:
    print(f"Ocorreu um erro: {e}")