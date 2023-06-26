from datetime import date

from utils.helper import (date_to_string, string_to_date)
from utils.messages import info_message

class Client:
    counter: int = 1
    
    def __init__(
        self: object, name: str, cpf: str, 
        birth_date: str, email: str
        ) -> None:
        self.__client_code: int = Client.counter 
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birth_date: str = string_to_date(birth_date)
        self.__register_date: date = date.today()
        Client.counter += 1

    @property
    def client_code(self: object) -> int:
        return self.__client_code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def birth_date(self: object) -> str:
        return date_to_string(self.__birth_date)

    @property
    def register_date(self: object) -> str:
        return date_to_string(self.__register_date)
    
    def __str__(self) -> str:
        return info_message(
            f'Codigo: {self.client_code}\n'\
            f'Nome: {self.name}\n'\
            f'Data de Nascimento: {self.birth_date}\n'\
            f'Data de cadastro: {self.register_date}'
        )
        