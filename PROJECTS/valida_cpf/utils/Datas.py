from datetime import datetime

class Data:
    def __init__(self) -> None:
        self.sing_up_moment = datetime.today()
        
    def __str__(self) -> str:
        return self.format_data()
    
    def initial_month(self) -> list:
        months_in_year = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro",
            "novembro", "dezembro"
        ]
        sing_up_month = self.sing_up_moment.month
        return months_in_year[sing_up_month - 1]
    
    def day_in_week(self) -> None:
        days_in_week = [
            "segunda", "terça", "quarta",
            "quinta", "sexta", "sabado",
            "domingo"
        ]
        day_week = self.sing_up_moment.weekday()
        return days_in_week[day_week] 
    
    def format_data(self):
        formated_data = self.sing_up_moment.strftime(
            "%d/%m/%Y %H:%M"
        )
        return formated_data
    