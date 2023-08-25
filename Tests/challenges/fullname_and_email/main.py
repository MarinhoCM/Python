class Employee:
    def __init__(self, firstname: str, last_name: str) -> None:
        self.__firstname = firstname
        self.__lastname = last_name
        
    @property
    def firstname(self):
        return self.__firstname
    
    @property
    def lastname(self):
        return self.__lastname
    
    def fullname(self) -> str:
        fullname = (f"{self.firstname} {self.lastname}")
        return str(fullname)
    
    def email(self) -> str:
        return (
            f"{self.firstname.lower()}.{self.lastname.lower()}@company.com"
        )

