import re

class Telefone:
    def __init__(self, tel: str) -> None:
        if self.validate_tel(tel):
            self.number = tel
        else:
            raise ValueError(
                "Número incorreto!"
            )
        
    def __str__(self) -> str:
        return self.format()
    
    def validate_tel(self, tel: str) -> bool:
        default = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        res = re.findall(default, tel)
        if res:
            return True
        else:
            return False
        
    def format(self):
        default = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        res = re.search(default, self.number)
        format_numbers = (
            f'+{res.group(1)}({res.group(2)})'\
            f'{res.group(3)}-{res.group(4)}'
        )     
        return format_numbers   
    