nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura (m): ").replace(",","."))

if idade >= 12 and altura >= 1.15:
    print(f"{nome}, acesso liberado!")
else:
    print(f"{nome}, você não tem a idade suficiente ou não tem a altura mínima permitida!")