from datetime import datetime

data_hoje = datetime.now().strftime('%Y%m%d')

print(data_hoje)

hora_atual = datetime.now().strftime("%H:%M")
print(f"Hora atual: {hora_atual}")