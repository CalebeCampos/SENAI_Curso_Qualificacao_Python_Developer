usuario = {
    "nome": "João",
    "idade": 30,
    "email": "joao@example.com",
    "profissao": "Engenheiro"
}

# exibindo o dicionário original
print("Dicionário original:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")

# Alterando o valor da chave "idade"
usuario["idade"] = 31

# exibindo o dicionário após a alteração
print("\nDicionário após alteração da idade:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")

# alterando o valor da chave escolhida pelo usuário
chave_escolhida = input("\nDigite a chave que deseja alterar (nome, idade, email, profissao): ").strip().lower()
if chave_escolhida in usuario:
    novo_valor = input(f"Digite o novo valor para '{chave_escolhida}': ")
    usuario[chave_escolhida] = novo_valor
else:
    print(f"A chave '{chave_escolhida}' não existe no dicionário.")

# exibindo o dicionário após a alteração feita pelo usuário
print(f"\nDicionário após alteração de '{chave_escolhida}':")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")