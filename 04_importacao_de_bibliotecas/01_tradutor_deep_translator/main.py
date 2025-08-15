from deep_translator import GoogleTranslator
# pip install deep_translator
import os

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    tradutor = GoogleTranslator(
        source="auto", # esse parametro identifica automaticamente o idioma do texto de entrada
        target="pt" # esse parametro identifica o idioma do texto de saida que sera traduzido
    )

    while True:
        print(f"\n{'-'*20} TRADUTOR {'-'*20}")
        print("1 - Informar texto")
        print("2 - Sair do programa")
        opcao = input("Opcao desejada: ").strip()
        limpar_terminal()

        match opcao:
            case "1":
                try:
                    texto_entrada = input("Informe o texto: ")
                    texto_saida = tradutor.translate(texto_entrada)
                    print(f"{'-'*20} TEXTO TRADUZIDO PARA PT {'-'*20}")
                    print(texto_saida)
                except Exception as e:
                    print(f"Nao foi possivel traduzir o texto. Erro: {e}")
                continue
            case "2":
                print("Programa finalizado!")
                break
            case _:
                continue


if __name__ == "__main__":
    main()