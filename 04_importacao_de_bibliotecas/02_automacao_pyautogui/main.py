import pyautogui as gui
import time

def main():

    gui.PAUSE = 1
    gui.press("win") # preciona a tecla win
    gui.write("bloco de notas") # digita o texto bloco de notas
    gui.press("enter") # preciona a tecla enter
    time.sleep(1)
    gui.hotkey("ctrl","t") # preciona teclas de atalho ctrl + t
    gui.write("Ola mundo!") # digita o texto ola mundo


if __name__ == "__main__":
    main()