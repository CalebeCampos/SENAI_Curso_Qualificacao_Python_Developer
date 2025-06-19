
# lista de nomes
nomes = ["Alice", "Bob", "Charlie", "David", "Eve"]

# imprimindo a lista original
print(f"Lista original: {nomes}")

# imprimindo o valor de um elemento da lista
print(f"Primeiro elemento: {nomes[0]}")
print(f"Segundo elemento: {nomes[1]}")
print(f"Terceiro elemento: {nomes[2]}")
print(f"Quarto elemento: {nomes[3]}")
print(f"Quinto elemento: {nomes[4]}")

# imprimindo o tamanho da lista
print(f"Tamanho da lista: {len(nomes)}")

# imprimindo a lista com um loop for
print("Lista com loop for:")
for nome in nomes:
    print(nome)




# lista de números com um elemento que é uma lista
lista_numeros = [1, 2, 3, [6, 7, 8, 9], 5]
print(f"Lista original: {lista_numeros}")
for numero in lista_numeros:
    if type(numero) is list:
        for n in numero:
            print(n)
    else:
        print(numero)

