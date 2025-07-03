try:
        
    nome_arquivo_informado = input("Informe o nome do arquivo (sem extensao): ").strip().lower()
    diretorio_arquivo_informado = input("Informe o diretorio onde este arquivo está salvo: ").strip()


    # abre o arquivo ja gravado em modo read (de leitura)
    with open(f"{diretorio_arquivo_informado}{nome_arquivo_informado}.txt", "r", encoding="utf-8") as t:
        texto_arquivo_informado = t.read()
    # exibe o conteudo do arquivo ja gravado
    print(f"Conteudo original do arquivo:\n{texto_arquivo_informado}")


    novo_texto = input("Digite o novo texto a ser salvo: \n")
    texto_original_mais_novo_texto = f"{texto_arquivo_informado}\n{novo_texto}"
    # abre o arquivo ja gravado em modo write (de edicao)
    with open(f"{diretorio_arquivo_informado}{nome_arquivo_informado}.txt", "w", encoding="utf-8") as t:
        t.write(texto_original_mais_novo_texto) # altera o conteudo do arquivo txt mantendo o texto original e adicionando o novo texto
    print(f"Novo texto adicionado com sucesso!")


    # abre o arquivo ja gravado em modo read (de leitura)
    with open(f"{diretorio_arquivo_informado}{nome_arquivo_informado}.txt", "r", encoding="utf-8") as t:
        texto_arquivo_apos_alteracao = t.read()
    # exibe o conteudo do arquivo apos alteracao
    print(f"Conteudo apos alteracao do arquivo:\n{texto_arquivo_apos_alteracao}")


except Exception as e:
    print(f"Nao foi possivel alterar o arquivo. Erro: {e}")