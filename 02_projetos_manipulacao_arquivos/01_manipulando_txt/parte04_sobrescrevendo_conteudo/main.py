import os

try:
        
    nome_arquivo_informado = input("Informe o nome do arquivo (sem extensao): ").strip().lower()
    diretorio_arquivo_informado = input("Informe o diretorio onde este arquivo está salvo: ").strip()

    # abre o arquivo ja gravado em modo read (de leitura)
    with open(f"{diretorio_arquivo_informado}/{nome_arquivo_informado}.txt", "r", encoding="utf-8") as t:
        texto_arquivo_informado = t.read()
    # exibe o conteudo do arquivo ja gravado
    print(texto_arquivo_informado)


    novo_texto = input("Digite o novo texto a ser salvo: \n")
    # abre o arquivo ja gravado em modo write (de edicao)
    with open(f"{diretorio_arquivo_informado}/{nome_arquivo_informado}.txt", "w", encoding="utf-8") as t:
        t.write(novo_texto)
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Novo texto salvo com sucesso!")


except Exception as e:
    print(f"Nao foi possivel alterar o arquivo. Erro: {e}")