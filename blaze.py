import pyautogui as pg
from time import sleep


def botao():
    sleep(0.3)
    pg.moveTo('azul.PNG')
    pg.click()
    sleep(0.1)
    pg.moveTo('vermelho.PNG')
    pg.click()
    print('certo')
    botao()


def rodar():
    while True:
        try:
            botao()

        except:
            print("Buscando...")


rodar()
