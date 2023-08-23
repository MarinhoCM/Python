class Employee:
    def __init__(self, firstname: str, last_name: str) -> None:
        self.__firstname = firstname
        self.__last_name = last_name
        
    @property
    def firstname(self):
        return self.__firstname
    
    @property
    def last_name(self):
        return self.__last_name
    
    def fullname(self) -> str:
        return f"{self.firstname} {self.last_name}"
    
    def email(self) -> str:
        return (
            f"{self.firstname.lower()}.{self.last_name.lower()}@company.com"
        )
