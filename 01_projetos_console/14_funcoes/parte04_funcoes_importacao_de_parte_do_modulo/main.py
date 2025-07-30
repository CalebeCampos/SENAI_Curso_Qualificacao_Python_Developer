# importando funções específicas de um módulo
from modulo import limpar_terminal, calcular_velocidade_media, calcular_aceleracao_media

# algoritmo principal
if __name__ == "__main__":

    while True:
        print("1. Calcular Velocidade Média")
        print("2. Calcular Aceleração Média")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()
        limpar_terminal()

        match opcao:
            case "1":
                try:
                    vi = float(input("Informe a velocidade inicial (m/s): ").strip().replace(',', '.'))
                    vf = float(input("Informe a velocidade final (m/s): ").strip().replace(',', '.'))
                    vm = calcular_velocidade_media(vi, vf)
                    limpar_terminal()
                    print(f"Velocidade Média: {vm} m/s")
                except Exception as e:
                    limpar_terminal()
                    print(f"Erro ao calcular velocidade média: {e}")
                finally:
                    continue
            case "2":
                try:
                    if 'vm' not in locals():
                        print("Primeiro, calcule a velocidade média.")
                    else:
                        # vm = float(input("Informe a velocidade média (m/s): ").strip().replace(',', '.'))
                        tm = float(input("Informe o tempo médio (s): ").strip().replace(',', '.'))
                        am = calcular_aceleracao_media(vm, tm)
                        limpar_terminal()
                        print(f"Aceleração Média: {am} m/s²")
                except Exception as e:
                    limpar_terminal()
                    print(f"Erro ao calcular aceleração média: {e}")
                finally:
                    continue
            case "3":
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue