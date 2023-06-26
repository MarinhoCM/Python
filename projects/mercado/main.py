from models.products import Product
from utils.helper import format_float_to_string
from utils.messages import (
    sucess_message, error_message, info_message
)

from time import sleep
from typing import List, Dict

products: List[Product] = []
shopping_cart: List[Dict[Product, int]] = []

def main() -> None:
    menu()
    
def menu() -> None:
    print(20*'='+20*'='+20*'=')
    print(23*'='+sucess_message(' Bem Vindo(a) ')+23*'=')
    print(23*'='+sucess_message(" Marin's Shop ")+23*'=')
    print(20*'='+20*'='+20*'=')
    
    print(
        info_message(
            'Selecione uma opção abaixo:\n'
            '1 - Cadastrar Produtos\n'\
            '2 - Listar Produtos\n'\
            '3 - Comprar Produtos\n'\
            '4 - Visualizar Carrinho\n'\
            '5 - Fechar Pedido\n'\
            '6 - Sair Do Sistema\n'
        )
    )
    option: int = int(input(info_message('--> '))) 
     
    if option == 1:
        insert_product()
    elif option == 2:
        list_product()
    elif option == 3:
        buy_product()
    elif option == 4:
        view_shopping_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print(sucess_message('Volte Sempre!'))
        sleep(2)
        exit(0)
    else:
        print(error_message('Opção Inválida!'))
        menu()
     
def insert_product() -> None:
    print(
        info_message(
            ' Cadastro de Produto:\n'
        ), '========================'
        
    )
    name: str = str(input(info_message('Informe o nome do produto: ')))
    price: float = float(input(info_message('Informe o preço do produto: ')))
    product: Product = Product(name, price)
    products.append(product)
    print(
        info_message(
            f'O produto: {product.name} foi cadastrado com sucesso!'
        )
    )
    sleep(2)
    menu()
    
def list_product() -> None:
    if len(products) > 0:
        print(info_message(
            'Listagem de produtos:\n'),
            '========================'
        )
        for product in products:
            print(product)
            print('========================')
            sleep(1)
    else:
        print(error_message(
            'Ainda Não existem produtos cadastrados.')
        )
    sleep(2)
    menu()      
    
def buy_product() -> None:
    if len(products) > 0:
        print(info_message(
            'Informe o codigo do produto que deseja adicionar ao carrinho:'
        ))
        print(
            '==========================='\
            '===================================='
        )
        print(sucess_message(30*'='+'Produtos Disponiveis'+30*'='))
        for product in products:
            print(product)
            print(40*'=')
            sleep(1)
        code: int = int(input()) 
        product: Product = get_product_by_code(code)
        
        if product:
            if len(shopping_cart) > 0:
                in_shopping_cart: bool = False
                for item in shopping_cart:
                    quantity: int = item.get(product)
                    if quantity:
                        item[product] = quantity + 1
                        print(sucess_message(
                            f'O produto: {product.name} agora '\
                            f'possui {quantity + 1} unidades no carrinho.'
                        ))
                if not in_shopping_cart:
                    prod = {product: 1}
                    shopping_cart.append(prod)
                    print(sucess_message(
                        f'O produto: {product.name} '\
                        'foi adcionado ao carrinho.'
                    ))
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                shopping_cart.append(item)
                print(sucess_message(
                    f'O produto {product.name} foi adcionado ao carrinho.'
                ))
                sleep(2)
                menu()
        else:
            print(error_message(
                f'O produto com código {code} não foi encontrado!'
            ))
    else:
        print(error_message('Ainda não existem produtos a venda.'))
    sleep(2)
    menu()
    
def view_shopping_cart() -> None:
    if len(shopping_cart) > 0:
        print(info_message(f'Produtos no carrinho:'))
        for item in shopping_cart:
            for data in item.items():
                print(data[0])
                print(info_message(f'Quantidade: {data[1]}'))
                print(f'======================')
                sleep(1)
    else:
        print(error_message(
            'Ainda não existem produtos no carrinho.'
        ))
    sleep(2)
    menu()

def close_order() -> None:
    if len(shopping_cart) > 0:
        total_value: float = 0
        print('Produtos do Carrinho:')
        for item in shopping_cart:
            for data in item.items:
                print(data[0])
                print(f'Quantidade: {data[1]}')
                total_value += data[0].price * data[1]
                print(40*'=')
                sleep(2)
        print(info_message(
            f'Sua fatura é: {format_float_to_string(total_value)}'
        ))
        print(sucess_message('Volte sempre!'))
        shopping_cart.clear()
        sleep(5)
        menu()
    else:
        print(error_message('Ainda não existem produtos no carrinho!'))
    sleep(2)
    menu()

def get_product_by_code(code: int) -> Product:
    p: Product = None
    for product in products:
        if product.cod == code:
            p = product
    return p

if __name__ == '__main__':
    main()
    