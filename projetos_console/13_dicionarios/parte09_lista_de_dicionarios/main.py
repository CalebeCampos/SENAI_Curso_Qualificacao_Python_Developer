usuarios = [
    {
        "nome": "Calebe Campos",
        "idade": 30,
        "profissao": "Desenvolvedor Python",
        "data_nascimento": "1993-05-15"
    },
    {
        "nome": "Maria Silva",
        "idade": 25,
        "profissao": "Analista de Sistemas",
        "data_nascimento": "1998-08-20"
    },
    {
        "nome": "Carlos Souza",
        "idade": 28,
        "profissao": "Designer Gráfico",
        "data_nascimento": "1995-02-10"
    }
]


# exibindo a lista de dicionários usando um loop for dentro de outro loop for
print("Lista de usuários:")
for usuario in usuarios:
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario[chave]}")
    print("\n")

# exibindo o valor de uma chave específica de um dicionário
print(usuarios[2]["profissao"])
print("\n")
print(usuarios[2].get("profissao"))
print("\n")