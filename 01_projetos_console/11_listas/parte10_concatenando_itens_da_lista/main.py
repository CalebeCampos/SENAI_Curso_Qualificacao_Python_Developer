dias_da_semana = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado"
]

# exibe os valores da lista
print("Elementos da lista dias da semana:")
for i in range(len(dias_da_semana)):
    print(f"Índice {i}: {dias_da_semana[i]}")
print('-'*60)


delimitador = " /\ "
dias_da_semana_concatenados = delimitador.join(dias_da_semana)
print(f"Dias da semana concatenados: {dias_da_semana_concatenados}")