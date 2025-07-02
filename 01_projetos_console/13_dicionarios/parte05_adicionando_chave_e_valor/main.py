usuario = {
    'nome': "João",
    'idade': 30,
    'email': "joao@example.com",
    'profissao': "Engenheiro"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("\n")

# adicionando nova chave e valor
usuario['telefone'] = "1234-5678"
usuario['endereco'] = input("Digite o endereço: ").strip()

# exibindo o dicionário atualizado
print("\nDicionário atualizado:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

