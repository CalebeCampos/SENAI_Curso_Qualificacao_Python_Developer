import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# funcao recursiva: sequencia de Fibonacci
# Fn = Fn-1 + Fn-2
def calcular_termo_fibonacci(termo):
    return termo if termo <= 1 else calcular_termo_fibonacci(termo - 1) + calcular_termo_fibonacci(termo - 2)
