import modulo as mo

if __name__ == '__main__':
    while True:
        print("Calculadora de Equações")
        print("1. Equação do 1º grau")
        print("2. Equação do 2º grau")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()
        mo.limpar_tela()
        match opcao:
            case "1":
                try:
                    a = float(input("Digite o valor de a: ").strip().replace(",", "."))
                    b = float(input("Digite o valor de b: ").strip().replace(",", "."))
                    mo.limpar_tela()
                    resultado = mo.calcular_equacao_primeiro_grau(a, b)
                    print(f"O valor de X para a equação {a}x + {b} = 0, é: {resultado}")
                except Exception as e:
                    print(f"Ocorreu um erro ao calcular a equação do 1º grau. Erro:{e}")
                finally:
                    continue
            case "2":
                try:
                    a = float(input("Digite o valor de a: ").strip().replace(",", "."))
                    b = float(input("Digite o valor de b: ").strip().replace(",", "."))
                    c = float(input("Digite o valor de c: ").strip().replace(",", "."))
                    mo.limpar_tela()
                    resultados = mo.calcular_equacao_segundo_grau(a, b, c)
                    for resultado in resultados:
                        print(f"{resultado}")
                except Exception as e:
                    print(f"Ocorreu um erro ao calcular a equação do 2º grau. Erro: {e}")
                finally:
                    continue
            case "3":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue
