class Football:
    def __init__(self, wins: int, draw: int, loses: int) -> None:
        self.__wins = wins
        self.__draw = draw
        self.__loses = loses
        
    @property
    def wins(self) -> int:
        return self.__wins
    
    @property
    def draw(self) -> int:
        return self.__draw
    
    @property
    def loses(self) -> int:
        return self.__loses
    
    def football_points(self) -> int:
        if (self.wins < 0 or self.draw < 0 or self.loses < 0):
            print("Enter a valid value!")
        else:
            points: int = (self.wins * 3) + (self.draw)
            return points