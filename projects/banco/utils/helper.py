from datetime import date
from datetime import datetime

def date_to_string(date: date) -> str:
    return date.strftime('%d/%m/%Y')

def string_to_date(date: str) -> date:
    return datetime.strptime(date, '%d/%m/%Y')

def format_float_to_string(value: str) -> str:
    return f'R$ {value:,.2f}'