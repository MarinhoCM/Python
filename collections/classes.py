from abc import (ABCMeta, abstractmethod)

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo) -> None:
        self._codigo = codigo
        self._saldo = 0
        
    def deposita(self, valor) -> None:
        self._saldo += valor
    
    def __str__(self) -> str:
        return (
            f"[>>Codigo {self._codigo} "\
            f"Saldo {self._saldo}<<]"
        )
    
    @abstractmethod        
    def passa_o_mes(self):
        self._saldo -= 2

        
class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3
  
        
class ContaSalario:
    def __init__(self, codigo) -> None:
        self._codigo = codigo
        self._saldo = 0
        
    def __eq__(self, __value: object) -> bool:
        return self._codigo == __value
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self) -> str:
        return (
            f"[>>Codigo {self._codigo} "\
            f"Saldo {self._saldo}<<]"
        )
        