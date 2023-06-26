import re
from validate_docbr import CPF

from .messages import error_message, info_message

def validate_cpf(cpf: str, reset) -> None:
    """
    Função responsável por validar o cpf dos clientes.
    """
    cpf_instance = CPF()
    cpf_result = cpf_instance.validate(cpf)
    if cpf_result:
        pass
    else:
        print(error_message('Insira um CPF válido.'))
        reset()

def validate_email(email: str, reset=None) -> None:
    """
    Função responsável por validar o email dos clientes.
    """
    default = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(default, email) is not None:
        pass
    else:
        print(error_message('Insira um E-mail válido.'))
        reset()

def validate_input_email() -> None:
    """
    Função responsável por validar o input do E-mail do cliente,
    se o email for inválido a função irá ser chamada novamente
    para que o usuário posso inserir o e-mail novamente.
    """
    email: str = str(input(info_message('E-mail do Cliente: '))).strip()
    validate_email(email, validate_input_email)
    return email 

def validate_input_cpf() -> None:
    """
    Função responsável por validar o input do CPF do cliente,
    se o CPF for inválido a função irá ser chamada novamente
    para que o usuário posso inserir o CPF novamente.
    """
    cpf: str = str(input(info_message('CPF do Cliente: '))).strip()
    validate_cpf(cpf, validate_input_cpf)
    return cpf 