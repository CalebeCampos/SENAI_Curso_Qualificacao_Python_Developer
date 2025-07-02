usuario = {
    "nome": "João",
    "idade": 30,
    "email": "joao@example.com",
    "profissao": "Engenheiro",
    "cidade": "São Paulo",
    "telefone": "1234-5678",
    "ativo": True,
    "genero": "Masculino",
    "data_nascimento": "1993-05-15"
}

# exibindo o dicionário original
print("Dicionário original:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# removendo a chave "email" usando pop
usuario.pop("email", None)

# exibindo o dicionário após a remoção
print("\nDicionário após remoção do email:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")


# pop() remove um item específico e retorna o valor associado, enquanto del remove o item sem retornar valor

# removendo a chave escolhida pelo usuário usando del
chave_escolhida = input("\nDigite a chave que deseja remover (nome, idade, profissao, cidade, telefone, ativo, genero, data_nascimento): ").strip().lower()
if chave_escolhida in usuario:
    del usuario[chave_escolhida]
    print(f"A chave '{chave_escolhida}' foi removida com sucesso.")
else:
    print(f"A chave '{chave_escolhida}' não existe no dicionário.")

# exibindo o dicionário após a remoção feita pelo usuário
print(f"\nDicionário após remoção de '{chave_escolhida}':")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")