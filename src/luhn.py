def luhn_check(card_number):
    digits = [int(d) for d in str(card_number) if d.isdigit()]
    control = digits.pop()

    parity = (len(digits) + 1) % 2
    total = 0
    for i in range(len(digits)):
        doubled = digits[i]

        if i % 2 == parity:
            doubled = doubled * 2
            if doubled > 9:
                doubled = doubled - 9
        total += doubled
    
    return (total + control) % 10 == 0

