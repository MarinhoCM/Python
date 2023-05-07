from FilaBase import FilaBase
from constantes import CODIGO_PRIORITARIO

from typing import Dict


class FilaPrioritaria(FilaBase):
    def __init__(self)-> None:
        self.codigo : int = 0
        self.fila : list = []
        self.clientes_atendidos : list = []
        self.senha_atual : str = ''

    def gerar_senha_atual(self)-> None:        
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'
    
    def reseta_fila(self)-> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
    
    def atualiza_fila(self)-> None:
        self.reseta_fila()
        self.gerar_senha_atual()
        self.fila.append(self.senha_atual)
        
    def chama_client(self, caixa: int)-> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual},'
                +f' dirija-se ao caixa: {caixa}'
        )
    
    def estatisticas(self, dia: str, agencia: int, flag: str)-> dict:
        if flag != 'detail':
            estatistica = {
                f'{agencia} - {dia}' : len(self.clientes_atendidos)
            }
        else: 
            estatistica : Dict[str, str] = {}
            estatistica['dia'] = str(dia)
            estatistica['agencia'] = str(agencia)
            estatistica['quantidade_clientes_atendidos'] = len(
                self.clientes_atendidos
            )
        return estatistica
    