cidades = [
    'São Paulo', 
    'Rio de Janeiro', 
    'Belo Horizonte', 
    'Curitiba', 
    'Porto Alegre',
    'Salvador',
    'Fortaleza',
    'Brasília',
    'Recife',
    'Manaus',
    'Belém',
    'Goiânia',
    'Campinas',
    'São Luís',
    'Brasília',
    'Maceió',
    'Natal',
    'Teresina',
    'João Pessoa',
    'Aracaju',
    'Cuiabá',
    'Brasília',
    'Campo Grande',
    'Florianópolis',
    'Brasília',
    'Vitória',
    'Palmas'
]

# solicitando ao usuário o nome da cidade que deseja pesquisar
cidade_pesquisa = input("Digite o nome da cidade que deseja pesquisar: ").title().strip()


# verificando se a cidade está na lista
if cidade_pesquisa in cidades:
    print(f"A cidade '{cidade_pesquisa}' está na lista.")
else:
    print(f"A cidade '{cidade_pesquisa}' não está na lista.")


# verificando quantas vezes a cidade aparece na lista
quantidade = cidades.count(cidade_pesquisa)
print(f"A cidade '{cidade_pesquisa}' aparece {quantidade} vezes na lista.")

# imprimindo o índice da primeira ocorrência da cidade na lista
if quantidade > 0:
    indice_cidade_pesquisada = cidades.index(cidade_pesquisa)
    print(f"A primeira ocorrência da cidade '{cidade_pesquisa}' está no índice {indice_cidade_pesquisada}.")
