# entrada de dados
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: ").replace(",","."))
altura = float(input("Informe sua altura (m): ").replace(",","."))

# saida de dados
print(f"Seja bem vindo, {nome}!")
print(f"Tipo do dado da variavel 'nome': {type(nome)}")
print(f"A sua idade é: {idade}")
print(f"Tipo do dado da variavel 'idade': {type(idade)}")
print(f"A sua altura é: {altura}")
print(f"Tipo do dado da variavel 'altura': {type(altura)}")
