import json

pessoa = {}

try:

    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
    # diretorio: 02_projetos_manipulacao_arquivos/02_manipulando_json/

    ######################################################################
    ##########                LENDO O ARQUIVO JSON              ##########
    ######################################################################

    # lendo o arquivo json e dessarializa em um dicionario do python
    with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
        pessoas = json.load(t) # cria a lista de dicionarios em python

    ######################################################################
    ##########         ADICIONANDO NOVO ITEM NA LISTA           ##########
    ######################################################################

    # usuário informa os dados da nova pessoa
    pessoa['nome'] = input("Informe o nome: ").strip().title()
    pessoa['idade'] = int(input("Informe a idade: "))
    pessoa['cpf'] = input("Informe o CPF: ").strip()
    pessoa['rg'] = input("Informe o RG: ").strip()
    pessoa['data_nasc'] = input("Informe a data de nascimento: ").strip()
    pessoa['sexo'] = input("Informe o gênero: ").strip()
    pessoa['signo'] = input("Informe o signo: ").strip().capitalize()
    pessoa['mae'] = input("Informe o nome da mãe: ").strip().title()
    pessoa['pai'] = input("Informe o nome da pai: ").strip().title()
    pessoa['email'] = input("Informe o e-mail: ").strip().lower()
    pessoa['senha'] = input("Informe a senha: ")
    pessoa['cep'] = input("Informe o CEP: ").strip()
    pessoa['endereco'] = input("Informe o endereço: ").strip().title()
    pessoa['numero'] = int(input("Informe o número do endereço: "))
    pessoa['bairro'] = input("Informe o bairro: ").strip().capitalize()
    pessoa['cidade'] = input("Informe a cidade: ").strip().title()
    pessoa['estado'] = input("Informe o estado: ").strip().upper()
    pessoa['telefone_fixo'] = input("Informe o telefone: ").strip()
    pessoa['celular'] = input("Informe o celular: ").strip()
    pessoa['altura'] = float(input("Informe a altura: ").replace(",", "."))
    pessoa['peso'] = float(input("Informe o peso: ").replace(",", "."))
    pessoa['tipo_sanguineo'] = input("Informe o tipo sanguíneo: ").strip().capitalize()
    pessoa['cor'] = input("Informe a cor favorita: ").strip()

    # adiciona a nova pessoa na lista pessoas
    pessoas.append(pessoa)

    ######################################################################
    ##########            GRAVANDO A ALTERAÇÃO DA LISTA         ##########
    ######################################################################

    with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
        json.dump(pessoas, t, ensure_ascii=False, indent=4)

    ######################################################################
    ##########  LENDO O ARQUIVO JSON NOVAMENTE APOS ALTERACAO   ##########
    ######################################################################

    # lendo o arquivo json novamente apos gravacao da alteracao
    with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
        pessoas = json.load(t) # cria a lista de dicionarios em python

    # saida dos dados
    print(f"{'-'*20} LISTA DE PESSOAS {'-'*20}")
    for pessoa in pessoas:
        for chave in pessoa:
            print(f"{chave.capitalize()}: {pessoa.get(chave)}")
        print('-'*40)

except Exception as e:
    print(f"Nao foi possivel alterar o arquivo json. Erro: {e}")