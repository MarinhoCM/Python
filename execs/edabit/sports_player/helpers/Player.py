class Player:
    def __init__(
        self: object, name: str, age: int, height: float, weight: float
    ) -> None:
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def age(self: object) -> str:
        return self.__age

    @property
    def height(self: object) -> str:
        return self.__height

    @property
    def weight(self: object) -> str:
        return self.__weight

    def get_age(self: object) -> str:
        return f"{self.name.title()} is age {self.age}"

    def get_height(self: object) -> int:
        return f"{self.name.title()} is {self.height:.0f}cm"

    def get_weight(self: object) -> int:
        return f"{self.name} weights {self.weight:.0f}Kg"
