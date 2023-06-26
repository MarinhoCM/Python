from colorama import init, Fore, Style
from configs.colorama_install import install_colorama
from utils.calculator_functions import *


class Calculator:
    def __init__(self):
        install_colorama()
        init()
        Calculator.select_options()
    
    def select_options():
        option = int(
            input(
                Fore.GREEN+"Selecione uma operação:"+
                "\n[1] - SOMAR\n[2] - SUBTRAIR"+
                "\n[3] - MULTIPLICAR\n[4] - DIVIDIR\n"+
                ">>>>> "+Style.RESET_ALL
            ))        
        
        if option == 1:
            print("Operação selecionada: SOMAR")
            adding()
        elif option == 2:
            print("Operação selecionada: SUBTRAIR")
            subtracting()
        elif option == 3:
            print("Operação selecionada: MULTIPLICAR")
            multiplying()
        elif option == 4:
            print("Operação selecionada: DIVIDIR")
            dividing()
        else:
            print("A operação selecionada é inválida.")
           
calc = Calculator()
