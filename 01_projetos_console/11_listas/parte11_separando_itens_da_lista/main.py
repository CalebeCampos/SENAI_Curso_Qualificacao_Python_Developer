texto_com_os_meses = "Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro"

# exbindo o texto com os meses
print(f"String com o nome dos meses: {texto_com_os_meses}")
print('-'*60)

# separando os meses em uma lista
meses = texto_com_os_meses.split(", ")

# exbibindo os meses da lista
print("Lista com os meses:")
for mes in meses:
    print(mes)
print('-'*60)

