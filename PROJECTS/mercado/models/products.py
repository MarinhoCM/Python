from utils.helper import format_float_to_string

class Product:
    counter: int = 1
    
    def __init__(self: object, name: str, price: float) -> None:
        self.__cod: int = Product.counter
        self.__name: str = name
        self.__price: float = price  
        Product.counter += 1
        
    @property
    def cod(self: object) -> int:
        return self.__cod
    
    @property
    def name(self: object) -> str:
        return self.__name
    
    @property
    def price(self: object) -> float:
        return self.__price
    
    def __str__(self) -> str:
        return (
            f'Código: {self.cod}\n '\
            f'Nome: {self.name}\n '\
            f'Preço: {format_float_to_string(self.price)}\n '
        )
        