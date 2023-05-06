import abc
# quebra de linha para diferenciar import do python e import do projeto
from constantes import (TAMANHO_PADRAO_MAXIMO,
                        TAMANHO_PADRAO_MINIMO)


class FilaBase(metaclass=abc.ABCMeta):
    def __init__(self)-> None:
        self.codigo: int = 0
        self.fila: list = []
        self.clientes_atendidos: list = []
        self.senha_atual: str = ''

    def reseta_fila(self)-> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1
    
    @abc.abstractmethod        
    def gerar_senha_atual(self)-> None: #  obrigando as classes filhas
                                        #  a escreverem o metodo   
        ...
    
    @abc.abstractmethod                
    def atualiza_fila(self)-> None:
        ...
        
    @abc.abstractmethod                
    def chama_client(self, caixa : int)-> str:
        ...