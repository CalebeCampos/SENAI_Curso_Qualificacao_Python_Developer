import json

try:
    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
    # diretorio: 02_projetos_manipulacao_arquivos/02_manipulando_json

    # lendo o arquivo json e dessarializa em um dicionario do python
    with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
        lista = json.load(t) # cria a lista de dicionarios em python

    # alterando a altura e o peso de todos os itens da lista
    for item in lista:
        item['altura'] = item['altura'].replace(",",".") # substitui a virgula por ponto na altura de todos os itens da lista
        item['altura'] = float(item['altura']) # converte o valor da altura para de string para float para todos os itens da lista
        item['peso'] = float(item['peso']) # converte o valor do peso de inteiro para float para todos os itens da lista

    print(f"{'-'*20} DADOS DOS ITENS DA LISTA {'-'*20}")
    for item in lista:
        for chave in item:
            print(f"{chave}: {item.get(chave)}")
        print('-'*50)
    
except Exception as e:
    print(f"Nao foi possivel alterar o arquivo json. Erro: {e}")