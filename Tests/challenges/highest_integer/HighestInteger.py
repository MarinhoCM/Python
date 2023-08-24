from typing import List

class HighestInteger:
    def __init__(self, number_list: List[int]) -> None:
        self.__number_list = number_list
    
    @property
    def number_list(self) -> object:
        return self.__number_list
    
    def find_highest_integer(self) -> int:
        higher: int = 0
        for i in set(self.number_list):
            if i > higher:
                higher = i
        return higher
