
print(f"{"="*10} ESCOLHA UMA OPERAÇÃO {"="*10}")
print("1 - soma")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")
print("\n")

operacao = input("Informe a operacao desejada: ").strip()
x = float(input("Informe o valor de X: ").replace(",","."))
y = float(input("Informe o valor de Y: ").replace(",","."))

match operacao:
    case "1":
        print(f"A soma de {x} e {y} é: {x+y}")
    case "2":
        print(f"A subtracao de {x} e {y} é: {x-y}")
    case "3":
        print(f"A multiplicacao de {x} e {y} é: {x*y}")
    case "4":
        print(f"A divisao de {x} e {y} é: {x/y}")
    case _: # para qualquer outra opcao...
        print("Operacao invalida!")