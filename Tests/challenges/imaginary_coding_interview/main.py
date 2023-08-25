from typing import List

class Interview:
    def __init__(self, time_list: List[int], max_time: int) -> None:
        self.__time_list = time_list
        self.__max_time = max_time
    
    @property
    def time_list(self) -> List[int]:
        return self.__time_list
    
    @property
    def max_time(self) -> int:
        return self.__max_time
    
    def interview(self) -> str:
        for i in self.time_list:
            if i > 20:
                return "disqualified"
            else:
                result = sum(self.time_list, 0)
                if result <= self.max_time:
                    return "qualified"
                else:
                    return "disqualified"
