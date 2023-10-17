def simple_coder(text: str) -> str:
    """Crie uma função que receba uma string str
    e execute uma codificação simples conforme o
    seguinte método:

    - Substitua todos os caracteres de ocorrência 
    única por [
    - Substitua todos os caracteres por duas ou 
    mais ocorrências com ]
    - Retorne a string final após a modificação."""
    
    texto_codificado = ""
    for caractere in text:
        if text.count(caractere) == 1:
            texto_codificado += '['
        else:
            texto_codificado += ']'

    return texto_codificado
