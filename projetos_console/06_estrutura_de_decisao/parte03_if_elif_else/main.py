aluno = input("Informe o nome do aluno: ")
media_final = float(input("Informe sua média final: ").replace(",","."))


if media_final >= 0 and media_final <= 10:
    if media_final < 5:
        print(f"O {aluno}, foi reprovado!")
    elif media_final < 7:
        print(f"O {aluno}, está de recuperação!")
    else: 
        print(f"O {aluno}, foi aprovado!")
else:
    print("Media invalida!")



