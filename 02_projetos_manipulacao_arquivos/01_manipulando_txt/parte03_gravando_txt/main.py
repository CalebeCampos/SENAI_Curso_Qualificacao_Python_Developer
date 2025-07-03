import os

while True:
    try:
        texto_novo_arquivo = input("Digite o texto a ser salvo: \n")
        nome_novo_arquivo = input("Informe o nome do arquivo (sem extensao): ").strip().lower()
        diretorio_novo_arquivo = input("Informe o diretorio onde este arquivo deverá ser salvo: ").strip()
        with open(f"{diretorio_novo_arquivo}{nome_novo_arquivo}.txt", "w", encoding="utf-8") as t:
            t.write(texto_novo_arquivo)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nome_novo_arquivo}.txt gravado com sucesso!")

        while True:

            prosseguir = input("Deseja gravar novo arquivo? (s/n): ").strip().lower()

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
        print(f"Nao foi possivel gravar o arquivo. Erro: {e}")
        continue