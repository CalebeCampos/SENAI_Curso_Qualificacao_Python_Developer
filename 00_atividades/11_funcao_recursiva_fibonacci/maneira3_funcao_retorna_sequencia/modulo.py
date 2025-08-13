import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
 
def gerar_sequencia_fibonacci(quantidade_termos):
    def calcular_termo_fibonacci(quantidade_termos):
        if quantidade_termos <= 1:
            return quantidade_termos
        else:
            return (calcular_termo_fibonacci(quantidade_termos-1) + calcular_termo_fibonacci(quantidade_termos-2))
    sequencia = []
    for i in range(1, quantidade_termos+1):
        termo_gerado = calcular_termo_fibonacci(i)
        sequencia.append(termo_gerado)
    return sequencia