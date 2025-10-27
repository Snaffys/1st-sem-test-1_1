def fast_pow(number, power):
    if (not isinstance(number, int)) and (not isinstance(number, float)):
        print("Error: number is not an integer!")
        return None
    if not isinstance(power, int):
        print("Error: power is not an integer!")
        return None
    if power < 0:
        print("Error: negative value!")
        return None

    if power == 0:
        return 1
    if power == 1:
        return number

    if number == 0:
        if power > 0:
            return 0
        print("undefined")
        return 0

    result = 1
    base = number

    while power > 0:
        if power % 2 == 1:
            result *= base
        base *= base
        power //= 2

    return result

