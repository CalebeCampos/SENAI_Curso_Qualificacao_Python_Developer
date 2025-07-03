import json

pessoa = {}

try:

    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
    # diretorio: 02_projetos_manipulacao_arquivos/02_manipulando_json

    ######################################################################
    ##########                LENDO O ARQUIVO JSON              ##########
    ######################################################################

    # lendo o arquivo json e dessarializa em um dicionario do python
    with open(f"{diretorio_arquivo}/{nome_arquivo}.json", "r", encoding="utf-8") as t:
        pessoas = json.load(t) # cria a lista de dicionarios em python

    ######################################################################
    ##########         ADICIONANDO NOVO ITEM NA LISTA           ##########
    ######################################################################



    ######################################################################
    ##########            GRAVANDO A ALTERAÇÃO DA LISTA         ##########
    ######################################################################
 
except Exception as e:
    print(f"Nao foi possivel alterar o arquivo json. Erro: {e}")