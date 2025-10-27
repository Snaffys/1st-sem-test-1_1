def luhn_check(card_number):
    card_number_str = str(card_number).replace(" ", "")

    if not card_number_str.isdigit():
        print("Error: must contain only digits!")
        return None

    if len(card_number_str) < 16:
        print("Error: must contain at least 16 digits!")
        return None

    digits = [int(d) for d in card_number_str]
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


def main():
    print("Enter card number to check validity")
    print("Enter '-1' to exit")

    while True:
        user_input = input("\nEnter card number: ").strip()

        if user_input == "-1":
            break

        if not user_input:
            print("Empty input!")
            continue

        result = luhn_check(user_input)
            
        if result is None:
            continue
        elif result:
            print("correct")
        else:
            print("incorrect")

if __name__ == "__main__":
    main()
    