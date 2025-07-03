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

    for chave, valor in pessoas[0].items():
        print(f"{chave}: {type(valor)} ==>> {"sim" if type(valor) == str else "nao"}")
    
    for chave, valor in pessoa[0].items():
        if type(valor) == str:
            pessoa[chave] = input(f"Informe o valor de '{chave.capitalize()}': ")
        elif type(valor) == int:
            pessoa[chave] = int(input(f"Informe o valor de '{chave.capitalize()}': ").strip())
        elif type(valor) == float:
            pessoa[chave] = float(input(f"Informe o valor de '{chave.capitalize()}': ").strip())


    for chave, valor in pessoa.items():
        print(f"{chave.capitalize()}: {valor}")

    ######################################################################
    ##########            GRAVANDO A ALTERAÇÃO DA LISTA         ##########
    ######################################################################
 
except Exception as e:
    print(f"Nao foi possivel alterar o arquivo json. Erro: {e}")