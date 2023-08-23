class Player:
    def __init__(
        self, name: str, age: int, height: int, weight: int
    ) -> None:
        self.__name = name
        self.__age = age
        self.__heigth = height
        self.__weight = weight
        
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def height(self) -> int:
        return self.__heigth
    
    @property
    def weight(self) -> int:
        return self.__weight

    def get_age(self) -> str:
        return (
            f"{self.name} is age {self.age}"
        )
    
    def get_height(self) -> str:
        return (
            f"{self.name} is {self.height}cm"
        )
    
    def get_weight(self) -> str:
        return (
            f"{self.name} weighs {self.weight}kg"
        )
