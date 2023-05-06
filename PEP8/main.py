from PEP8.FilaNormal import FilaNormal
from PEP8.FilaPrioritaria import FilaPrioritaria


class Main:
    def __init__(self) -> None:
        Main.fila_normal()
        Main.fila_prioritaria()
    
    def fila_normal(self= None) -> None:
        fila_normal = FilaNormal()
        fila_normal.atualiza_fila()
        fila_normal.atualiza_fila()
        fila_normal.atualiza_fila()
        print(fila_normal.chama_client(5))
        print(fila_normal.chama_client(10))

    def fila_prioritaria(self= None) -> None:
        fila_prioritaria = FilaPrioritaria()
        fila_prioritaria.atualiza_fila()
        fila_prioritaria.atualiza_fila()
        fila_prioritaria.atualiza_fila()
        print(fila_prioritaria.chama_client(1))
        print(fila_prioritaria.chama_client(3))
        print(fila_prioritaria.estatisticas('06/05/2023',
                                            198,
                                            'detail'))

Main()
