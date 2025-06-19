"""
# TODO - atividade: Crie um programa que mostre a hora atual sempre sendo atualizada a cada segundo.
# NOTE - para interromper o programa, use a tecla de atalho Ctrl+C
"""

import os
import time
import datetime as dt

while True:
    hora = dt.datetime.now().strftime("%H:%M:%S")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Hora atual: {hora}")
    time.sleep(1)
    