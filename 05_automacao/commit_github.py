import pyautogui as gui
import time

def main():

    usuario = input("Informe seu usuario do gitHub: ").strip()
    email = input("Informe seu email do gitHub: ").strip()
    data_commit = input("Informe a data do commit: ").strip()
    hora_commit = input("Informe a hora do commit: ").strip()

    gui.PAUSE = 0.5

    gui.hotkey("win","r") # abrir o executar
    gui.write('cmd') # digita o texto cmd
    gui.press("enter") # preciona a tecla enter
    gui.write('cd C:\\Users\\ead\\PythonDev_CalebeCampos')
    gui.press("enter") # preciona a tecla enter
    gui.write('git config --global --unset user.name')
    gui.press("enter") # preciona a tecla enter
    gui.write('git config --global --unset user.email')
    gui.press("enter") # preciona a tecla enter
    gui.write(f'git config --global user.name "{usuario}"')
    gui.press("enter") # preciona a tecla enter
    gui.write(f'git config --global user.email "{email}"')
    gui.press("enter") # preciona a tecla enter
    gui.write('git add .')
    gui.press("enter") # preciona a tecla enter
    gui.write(f'git commit -m "arquivos criados e alterados até o dia {data_commit} as {hora_commit}"')
    gui.press("enter") # preciona a tecla enter
    gui.write('git push')
    gui.press("enter") # preciona a tecla enter


#    gui.press("win") # preciona a tecla win
#    gui.write("bloco de notas") # digita o texto bloco de notas
#    time.sleep(1)
#    gui.write("Ola mundo!") # digita o texto ola mundo


if __name__ == "__main__":
    main()