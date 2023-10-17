def count_the_digits(number: int) -> int:
    if number == 0:
        return 1

    counter = 0
    number = abs(number)

    while number > 0:
        counter += 1
        number //= 10
    return counter