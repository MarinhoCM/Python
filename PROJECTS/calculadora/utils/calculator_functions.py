def adding():
    number_one = int(input("\033[32mDigite um número:\033[0m "))
    number_two = int(input("\033[32mDigite outro número:\033[0m "))
    try:
        added = int(number_one + number_two)
    
    except:
        raise Exception("\033[33mNão foi", 
                        "possivel fazer essa operação\033[0m")
    
    print(f"\033[32O Resultado da soma entre:",
          f"({number_one} e {number_two})",
          f"é: {added}\033[0m")       

def subtracting():
    number_one = int(input("\033[32mDigite um número:\033[0m "))
    number_two = int(input("\033[32mDigite outro número:\033[0m "))
    try:
        subtracted = int(number_one - number_two)
    
    except:
        raise Exception("\033[33mNão foi", 
                        "possivel fazer essa operação\033[0m")
    
    print(f"\033[32O Resultado da subtração entre:",
          f"({number_one} e {number_two})",
          f"é: {subtracted}\033[0m")       

def multiplying():
    number_one = int(input("\033[32mDigite um número:\033[0m "))
    number_two = int(input("\033[32mDigite outro número:\033[0m "))
    try:
        multiplied = int(number_one * number_two)
    
    except:
        raise Exception("\033[33mNão foi", 
                        "possivel fazer essa operação\033[0m")
    
    print(f"\033[32O Resultado da multiplicação entre:",
          f"({number_one} e {number_two})",
          f"é: {multiplied}\033[0m")       

def dividing():
    number_one = int(input("\033[32mDigite um número:\033[0m "))
    number_two = int(input("\033[32mDigite outro número:\033[0m "))
    try:
        divided = int(number_one / number_two)
    except ZeroDivisionError:
        print(f"\033[33mNão é possível dividir",
              f"{number_one} por {number_two} !\033[0m")
        return None
    else:
        print(f"\033[32mO resultado da divisão entre",
              f"{number_one} e {number_two} é: {divided}\033[0m")
        