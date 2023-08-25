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
        points: int = (self.wins * 3) + (self.draw)
        return points