import modulo as m

if __name__ == "__main__":
    while True:
        try:
            print("1 - Calcular fatorial")
            print("2 - Sair")
            opcao = input("Escolha uma opcao: ").strip()
            match opcao:
                case "1":
                    n = float(input("Informe um numero inteiro positivo para calcular o fatorial: ").strip().replace(",", "."))
                    print(f"{n}! = {m.calcular_fatorial(n)}")
                case "2":
                    print("Saindo...")
                    break
                case _:
                    print("Opcao invalida. Tente novamente.")
                    continue
            
        except Exception as e:
            print(f"Nao foi possivel executar a funcao. Erro: {e}")
    