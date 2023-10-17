def simple_coder(text: str) -> str:
    """Crie uma função que receba uma string str
    e execute uma codificação simples conforme o
    seguinte método:

    - Substitua todos os caracteres de ocorrência 
    única por [
    - Substitua todos os caracteres por duas ou 
    mais ocorrências com ]
    - Retorne a string final após a modificação."""
    
    text_code = ""
    for char in text:
        if text.count(char) == 1:
            text_code += '['
        else:
            text_code += ']'
    return text_code
