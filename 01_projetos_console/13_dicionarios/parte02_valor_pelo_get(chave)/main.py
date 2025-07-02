pessoa = {
    'nome': "João",
    'idade': 30,
    'email': "joao@example.com",
    'profissao': "Engenheiro"
}

# exibindo o valor de cada chave
print(f"Nome: {pessoa.get('nome')}")
print(f"Idade: {pessoa.get('idade')}")
print(f"E-mail: {pessoa.get('email')}")
print(f"Profissão: {pessoa.get('profissao')}")
# exibindo o valor de uma chave que nao existe
print(f"Telefone: {pessoa.get('telefone')}") # como nao existe, retorna None