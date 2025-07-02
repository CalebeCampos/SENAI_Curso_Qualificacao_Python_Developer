try:
    numero = int(input("Informe um numero inteiro: "))
    print(f"O numero informado é: {numero}")
except Exception as e:
    print(f"Não foi possivel executar o programa! Erro: {e}")