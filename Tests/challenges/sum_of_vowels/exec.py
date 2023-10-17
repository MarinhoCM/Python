def sum_of_vowels(text: str) -> int:
    """Crie uma função que receba uma string
    e retorne a soma das vogais , onde vogais
    são consideradas números.
    |Vogal|Número|
    |  A  |	 4   |
    |  E  |  3   |
    |  I  |  1   |
    |  O  |	 0   |
    |  U  |  0   |
    """
    counter = 0
    for i in text.upper():
        if i in "O" or i in "U":
            counter: int = counter + 0
        elif i in "A":
            counter: int = counter + 4
        elif i in "E":
            counter: int = counter + 3
        elif i in "I":
            counter: int = counter + 1
    return counter