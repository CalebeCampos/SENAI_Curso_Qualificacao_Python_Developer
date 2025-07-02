# = operador de atribuicao
# == operador de igualdade
# + operador de soma
# - operador de subtracao
# * operador de multiplicacao
# / operador de divisao
# // operador de divisao inteira, maior numero inteiro possivel na divisao
# % operador de modulo, resto da divisao
# ** operador de potenciacao
# > operador matematico de maior
# < operador matematico de menor
# >= operador matematico de maior ou igual
# <= operador matematico de menor ou menor
# <> operador de diferente de 
# != operador de diferente de
# += operador de atribuicao e adição
# -= operador de atribuicao e subtração
# *= operador de atribuicao e multiplicacao
# /= operador de atribuicao e divisao
# %= operador de atribuicao e resto da divisao
# **= operador de atribuicao e potenciacao
# and operador logico e
# or operador logico ou
# not operador logico de negacao
# is operador de identidade ou comparacao, retorna True ou False
# is not operador de nao identidade ou nao comparacao, retorna True ou False
# in operador de pertence, retorna True ou False
# in note operador de nao pertence, retorna True ou False

x = 5
y = 2
soma = x+y
subtracao = x-y
multiplicacao = x*y
divisao = x/y
resto_divisao = x%y
potencia = x**y

print("A soma das variaveis é:", x+y)
print("A subtracao das variaveis é:", x-y)

# convertendo o tipo da variavel
x = str(x)
y = str(y)
soma = str(soma)
subtracao = str(subtracao)

print("A soma das variaveis é: " + soma)
print("A subtracao das variaveis é: " + subtracao)


# concatenacao de strings (utilizando chaves {} com o format())
print("A soma de {} e {} é: {}".format(x, y, soma))
texto_string = "A soma de {} e {} é: {}"
print(texto_string.format(x, y, soma))

# concatenacao de strings (utilizando fstring)
print(f"A subtracao de {x} e {y} é: {subtracao}")
print(f"A multiplicacao de {x} e {y} é: {multiplicacao}")
print(f"A divisao de {x} e {y} é: {divisao}")
print(f"A o resto da divisao de {x} e {y} é: {resto_divisao}")
print(f"A potencia de {x} elevado a {y} é: {potencia}")