"""
Atividade 08 - Crie um programa que receba de um professor varias notas de um aluno, de 0 a 10. Ao final do programa, calcular a media das notas do aluno e me seguida o programa deverá informar:
- Se a média for maior ou igual a 7, o aluno foi aprovado.
- Se a média for entre 7 e 5, o aluno ficou de recuperacao.
- Se a média for menor que 5, o aluno foi reprovado.

"""

import os

notas = []

while True:

    print(f"{'-'*20} MENU {'-'*20}")
    print("1 - Adicionar nota")
    print("2 - Exibir lista de notas")
    print("3 - Calcular média")
    print("4 - Sair")
    opcao = input("Informe a opção desejada: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:

        # ADICIONAR NOTA
        case '1':
            try:
                nota = float(input("Digite a nota do aluno (0 a 10): ").replace(',', '.'))
                if nota < 0 or nota > 10:
                    print("Nota inválida. Deve ser entre 0 e 10.\n")
                else:
                    notas.append(nota)
                    print(f"Nota {nota} adicionada com sucesso!\n")
            except Exception as e:
                print(f"Nao foi possível adicionar a nota. Erro: {e}")
            finally:
                continue
        
        # EXIBIR LISTA DE NOTAS
        case '2':
            if not notas:
                print("Nenhuma nota cadastrada.\n")
            else:
                print("Lista de notas:")
                for nota in notas:
                    print(nota)
                print("\n")
            continue

        # CALCULAR MÉDIA
        case '3':
            try:
                media = sum(notas) / len(notas)
                print(f"Média das notas: {media:.2f}")

                if media >= 7:
                    print("O aluno foi aprovado.\n")
                elif media >= 5:
                    print("O aluno ficou de recuperação.\n")
                else:
                    print("O aluno foi reprovado.\n")

            except Exception as e:
                print(f"Nao foi possível calcular a média. Erro: {e}")
            finally:
                continue

        # SAIR DO PROGRAMA          
        case '4':
            print("Saindo do programa...\n")
            break

        case _:
            print("Opção inválida. Tente novamente.\n")

