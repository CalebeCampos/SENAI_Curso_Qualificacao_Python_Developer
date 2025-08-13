"""
Atividade 11: Função Recursiva Fibonacci
Desenvolva um programa que calcule o n-ésimo termo da sequência de Fibonacci utilizando uma função recursiva.
A sequência de Fibonacci é definida como:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2), para n > 1
"""

import modulo as m

if __name__ == "__main__":
    while True:
        try:
            print("1 - Calcular Fibonacci")
            print("2 - Sair")
            opcao = input("Escolha uma opcao: ").strip()
            m.limpar_terminal()
            match opcao:
                case "1":
                    termo = int(input("Informe o n-ésimo termo que deseja calcular: ").strip())
                    m.limpar_terminal()
                    print(m.calcular_termo_fibonacci(termo))
                case "2":
                    print("Saindo...")
                    break
                case _:
                    print("Opcao invalida. Tente novamente.")
                    continue
            
        except Exception as e:
            print(f"Nao foi possivel executar a funcao. Erro: {e}")