# importacoes
import os

# entrada de dados
while True:
    try:
        # usuario informa o nome do arquivo
        nome_arquivo_informado = input("Informe o nome do arquivo txt: ").strip().lower()
        # usuario informa o diretorio do arquivo
        diretorio_arquivo_informado = input("Informe o diretorio onde este arquivo está salvo: ").strip()
        # lendo o arquivo
        with open(f"{diretorio_arquivo_informado}/{nome_arquivo_informado}.txt", "r", encoding="utf-8") as t:
            arquivo_informado = t.read()
        os.system("cls" if os.name == "nt" else "clear")
        
        # imprimindo o conteudo do arquivo de texto
        print(arquivo_informado)

        while True:

            prosseguir = input("Deseja abrir outro arquivo? (s/n): ").strip().lower()

            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opcao invalida!")
                continue
        
        match prosseguir:
            case "s":
                continue
            case "n":
                break


    except Exception as e:
        print(f"Nao foi possivel ler o arquivo. Erro: {e}")
        continue
