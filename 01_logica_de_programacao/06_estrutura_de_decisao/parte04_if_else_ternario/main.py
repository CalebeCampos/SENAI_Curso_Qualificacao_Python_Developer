nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

# print(f"{nome}, você é menor de idade!") if idade < 18 else print(f"{nome}, acesso liberado!")
msg = "é menor de idade!" if idade < 18 else "é menor de idade!"
print(f"{nome} {msg}")

