from datetime import datetime
import pyautogui as gui
import time

def remover_credenciais():
    gui.write('git config --global --unset user.name')
    gui.press("enter") # preciona a tecla enter
    gui.write('git config --global --unset user.email')
    gui.press("enter") # preciona a tecla enter

def preencher_credenciais(usuario, email):
    gui.write(f'git config --global user.name "{usuario}"')
    gui.press("enter") # preciona a tecla enter
    gui.write(f'git config --global user.email "{email}"')
    gui.press("enter") # preciona a tecla enter

def main():

    usuario = input("Informe seu usuario do gitHub: ").strip()
    email = input("Informe seu email do gitHub: ").strip()
    data_atual = datetime.now().strftime('%Y%m%d')
    hora_atual = datetime.now().strftime("%H%M")
    mensagem_commit = f'git commit -m "arquivos criados e alterados ate o dia {data_atual} as {hora_atual}"'

    gui.PAUSE = 0.8

    gui.hotkey("win","r") # abrir o executar
    gui.write('cmd') # digita o texto cmd
    gui.press("enter") # preciona a tecla enter
    gui.write('cd C:\\Users\\ead\\PythonDev_CalebeCampos')
    gui.press("enter") # preciona a tecla enter
    remover_credenciais()
    preencher_credenciais(usuario, email)
    gui.write('git add .')
    gui.press("enter") # preciona a tecla enter
    gui.write(mensagem_commit)
    gui.press("enter") # preciona a tecla enter
    gui.write('git push')
    gui.press("enter") # preciona a tecla enter
    remover_credenciais()


if __name__ == "__main__":
    main()