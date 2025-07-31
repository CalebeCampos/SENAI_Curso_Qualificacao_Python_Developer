import math
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_equacao_primeiro_grau(a, b):
    # a*x + b = 0
    # x = -b / a
    return -b/a

def calcular_equacao_segundo_grau(a, b, c):
    # a*x^2 + b*x + c = 0
    # x = (-b ± sqrt(b^2 - 4*a*c)) / (2*a)
    if a is not 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
        # dessa forma, o yield retorna uma tupla com dois valores
            # yield x1, x2 
        # dessa forma, o yield retorna apenas um valor e depois o outro
            # yield x1 
            # yield x2
            yield f"x' = {x1}"
            yield f'x" = {x2}'
        elif delta == 0:
            yield "Não há raízes reais"
        else:
            x = -b / (2 * a)
            yield x
    else:
        yield calcular_equacao_primeiro_grau(b, c)