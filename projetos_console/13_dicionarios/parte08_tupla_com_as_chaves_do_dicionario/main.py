
# tupla com as chaves do dicionário
chaves = ('nome', 'idade', 'email', 'profissao', 'cidade', 'telefone', 'ativo', 'genero', 'data_nascimento')

# dicionário com as chaves da tupla e valores correspondentes
usuario = {
    chaves[0]: 'João',
    chaves[1]: 30,
    chaves[2]: 'joao@example.com',
    chaves[3]: 'Engenheiro',
    chaves[4]: 'São Paulo',
    chaves[5]: '1234-5678',
    chaves[6]: True,
    chaves[7]: 'Masculino',
    chaves[8]: '1993-05-15'
}

# exibindo o dicionário original
print("Dicionário original:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("\n")



