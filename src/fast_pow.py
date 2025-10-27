def fastPow(number, power):
    if (not isinstance(number, int)):
        printf("Error: number is not an integer!")
        return None
    if (not isinstance(power, int)):
        printf("Error: power is not an integer!")
        return None
    if power < 0:
        printf("Error: negative value!")
        return None

    if power == 0:
        return 1
    if power == 1:
        return number
    
    result = 1
    base = number

    while power > 0:
        if (power % 2 == 1):
            result *= base
        base *= base
        power //= 2

    return result
    
