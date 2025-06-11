nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

if idade < 18:
    print(f"{nome}, você é menor de idade, chame um responsavel!")
else:
    print(f"{nome}, acesso liberado!")
