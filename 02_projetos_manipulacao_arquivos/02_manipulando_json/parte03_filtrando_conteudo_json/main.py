import json

try:
    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
    # diretorio: 02_projetos_manipulacao_arquivos/02_manipulando_json

    # lendo o arquivo json e dessarializa em um dicionario do python
    with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
        conteudo_arquivo = json.load(t)

    # saida de dados
    print(f"{'-'*20} DADOS DO ARQUIVO JSON {'-'*20}")
    for item in conteudo_arquivo:
        print(f"Nome: {item.get('nome')}")
        print(f"Altura: {item.get('altura')}")
        print(f"Peso: {item.get('peso')}")
        print("-"*50)

except Exception as e:
    print(f"Nao foi possivel alterar o arquivo json. Erro: {e}")