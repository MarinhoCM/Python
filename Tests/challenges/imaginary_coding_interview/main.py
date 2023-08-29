from typing import List


class Interview:
    def __init__(self: object, time_list: List[int], max_time: int) -> None:
        self.__time_list = time_list
        self.__max_time = max_time
    
    @property
    def time_list(self) -> List[int]:
        return self.__time_list
    
    @property
    def max_time(self) -> int:
        return self.__max_time
    
    
    def verify_limit_spent_in_question(self: object) -> bool:
        times = self.time_list
        if (times[0] > 5) or (times[1] > 5):
            return False
        elif (times[2] > 10) or (times[3] > 10):
            return False
        elif (times[4] > 15) or (times[5] > 15):
            return False
        elif (times[6] > 20 ) or (times[7] > 20):
            return False
        else:
            return True
    
    
    def interview(self) -> str:
        if len(self.time_list) == 8 and self.max_time <= 120:
            if self.verify_limit_spent_in_question():
                result: int = sum(self.time_list, 0)
                result_with_tolerance_time: int = int(result - 20)
                if (result_with_tolerance_time) <= self.max_time:
                    return "qualified" 
                else:
                    return "disqualified"    
            else:
                return "disqualified"
        else:
            return "disqualified"
            