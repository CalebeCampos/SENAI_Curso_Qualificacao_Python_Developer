# lendo um arquivo txt
with open("02_projetos_manipulacao_arquivos/01_manipulando_txt/texto1.txt", "r", encoding="utf-8") as t:
    texto = t.read()

# saida de dados
print(texto)