from models.client import Client
from utils.helper import format_float_to_string
from utils.messages import (
    info_message, error_message, sucess_message
)

class Account:
    code: int = 1
    
    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.code
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self._calculate_total_balance
        Account.code += 1

    @property
    def number(self: object) -> int:
        return self.__number  
        
    @property
    def client(self: object) -> Client:
        return self.__client  
        
    @property
    def balance(self: object) -> float:
        return self.__balance
        
    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value
        
    @property
    def limit(self: object) -> float:
        return self.__limit
        
    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value
        
    @property
    def total_balance(self: object) -> float:
        return self.__total_balance
        
    @total_balance.setter
    def total_balance(self: object, value: float) -> float:
        self.__total_balance = value
    
    @property
    def _calculate_total_balance(self: object) -> float:
        return self.balance + self.limit
    
    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.balance = self.balance + value
            self.total_balance = self._calculate_total_balance
            print(sucess_message(
                'Depósito efetuado com sucesso!'
            ))
        else:
            print(error_message(
                'Erro ao efetuar deposito. Tente novamente.'
            ))
    
    def withdraw(self: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.limit = self.limit + remaining
                self.balance = 0
                self.total_balance = self._calculate_total_balance
            print(sucess_message(
                'Saque efetuado com sucesso!'
            ))
        else:
            print(error_message(
                'Saque não realizado. Tente novamente.'
            ))
    
    def transfer(self: object, destiny: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
                destiny.balance = destiny.balance + value
                destiny.total_balance = destiny._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.balance = 0
                self.limit = self.limit + remaining
                self.total_balance = self._calculate_total_balance
                destiny.balance = destiny.balance + value
                destiny.total_balance = destiny._calculate_total_balance
            print(sucess_message(
                'Transferência realizada com sucesso!'
            ))
        else:
            print(error_message(
                'Transrência não realizada. Tente novamente.'
            ))
        
    def __str__(self: object) -> str:
        return info_message(
            f'Número da conta: {self.number}\n'\
            f'{self.client}\n'\
            f'Saldo: {self.balance}\n'\
            f'Limite: {self.limit}\n'\
            f'Saldo Total: {format_float_to_string(self.total_balance)}'
        )
        