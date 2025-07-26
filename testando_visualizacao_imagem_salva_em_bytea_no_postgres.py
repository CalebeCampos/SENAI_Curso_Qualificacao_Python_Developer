import psycopg2
from PIL import Image
from io import BytesIO

# Conexão com o banco
conn = psycopg2.connect(
    host="127.0.0.1",
    database="citgrp_sefit_teste_v3",
    user="postgres",
    password="calebe"
)
cur = conn.cursor()

# Buscar uma imagem (ajuste o ID conforme seu caso)
cur.execute("select imagem from tb_gs_imagem where id_imagem = %s", (107,))
resultado = cur.fetchone()

if resultado:
    imagem_bytes = resultado[0]
    imagem = Image.open(BytesIO(imagem_bytes))
    imagem.show()  # Abre a imagem no visualizador padrão do sistema

cur.close()
conn.close()
