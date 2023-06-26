from typing import List
from time import sleep

from models.client import Client
from models.account import Account
from utils.messages import (
    sucess_message, info_message, error_message
)
from utils.validations import (
    validate_input_cpf, validate_input_email
)

accounts: List[Account] = []

def main() -> None:
    menu()
    
def menu(self=None) -> None:
    print(20*'='+20*'='+20*'=')
    print(27*'='+sucess_message(' ATM ')+28*'=')
    print(23*'='+sucess_message(" Marin's Bank ")+23*'=')
    print(20*'='+20*'='+20*'=')
        
    print(
        info_message(
            'Selecione uma opção abaixo:\n'
            '1 - Criar Conta\n'\
            '2 - Efetuar Saque\n'\
            '3 - Efetuar Depósito\n'\
            '4 - Efetuar Transferência\n'\
            '5 - Listar Contas\n'\
            '6 - Sair Do Sistema\n'
        )
    )
    option: int = int(input(info_message('--> '))) 
     
    if option == 1:
        create_account()
    elif option == 2:
        to_withdraw()
    elif option == 3:
        to_deposit()
    elif option == 4:
        to_transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print(sucess_message('Volte Sempre!'))
        sleep(2)
        exit(0)
    else:
        print(error_message('Opção Inválida!'))
        menu()
     
def create_account() -> None:
    print(info_message('Informe os dados do cliente:'))
    name: str = str(input(info_message('Nome do Cliente: '))).strip()
    email = validate_input_email()
    cpf = validate_input_cpf()
    birth_date: str = str (input(
        info_message('Data de Nascimento do Cliente: ')
        )
    ).strip()
    client: Client = Client(name, cpf, birth_date, email)
    account: account = Account(client)
    accounts.append(account)
    
    print(sucess_message('Conta criada com sucesso.'))
    print(info_message('Dados da Conta: '))
    print(23*'-')
    print(account)
    print(23*'-')
    sleep(2)
    menu()

def to_withdraw() -> None:
    if len(accounts) > 0:
        number: int = int(input(info_message(
            'Informe o número da sua conta: ')
            )
        )
        account: account = get_account_by_code(number)
        if account:
            value: float = float(input(info_message(
                'Informe o valor do saque: '
                ))
            )
            account.withdraw(value)
        else:
            print(error_message(
                f'Não foi possivel encontrar uma conta com número {number}.'
                )
            )
    else:
        print(error_message('Ainda não existem contas cadastradas.'))
    sleep(2)
    menu()
    
def to_deposit() -> None:
    if len(accounts) > 0:
        number: int = int(input(info_message(
            'Informe o número da sua conta: '
        )))
        account: account = get_account_by_code(number) 
        
        if account:
            value: float = float(input(info_message(
                'Informe o valor do depósito: '
            )))
            account.deposit(value)
        else:
            print(error_message(
                f'Não foi possivel encontrar uma conta com número {number}.'
            ))
    else:
        print(error_message(
            'Ainda não existem contas cadastradas.'
        ))
    sleep(2)
    menu()

def to_transfer() -> None:
    if len(accounts) > 0:
        number_origin: int = int(input(info_message(
            'Informe o número da sua conta: '
        )))
        account_origin: Account = get_account_by_code(number_origin)
        
        if account_origin:
            number_destiny: int = int(input(info_message(
                'Informe o número da conta destino: '
            ))) 
            account_destiny: Account = get_account_by_code(number_destiny)
            if account_destiny:
                value: float = float(input(info_message(
                    'Informe o valor da transferência: '
                )))
                account_origin.transfer(account_destiny, value)
            else:
                print(error_message(
                   f'A conta com número {account_destiny}'\
                    'não foi encontrada.'
                ))
        else:
            print(error_message(
                'Não foi possivel encontrar'\
                f' uma conta com número {number_origin}.'
            ))
    else:
        print(error_message(
            'Ainda não existem contas cadastradas.'
        ))
    sleep(2)
    menu()

def list_accounts() -> None: 
    if len(accounts) > 0:
        print(info_message('Listagem de Contas'))
        print(23*'-')
        for account in accounts:
            print(account)
            print(23*'-')
            sleep(1)
    else:
        print(error_message(
            'Não existem contas cadastradas.'
        ))
        
    sleep(2)
    menu()

def get_account_by_code(code: int) -> Account:
    ac: Account = None
    if len(accounts) > 0:
        for account in accounts:
            if account.number == code:
                ac = account
    return ac

if __name__ == '__main__':
    main()
    