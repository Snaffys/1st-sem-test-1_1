from src.luhn import luhn_check


def test_luhn_valid_card():
    assert luhn_check(4532015112830366) == True
    assert luhn_check(6011514433546201) == True
    assert luhn_check("4532 0151 1283 0366") == True


def test_luhn_invalid_card():
    assert luhn_check(4532015112830367) == False
    assert luhn_check(1234567812345678) == False


def test_luhn_short_number():
    assert luhn_check(123456789345) == None


def test_luhn_non_digits():
    assert luhn_check("4532-0151-1283-0366") == None
    assert luhn_check("4532abcd12830366") == None


def test_luhn_empty_string():
    assert luhn_check("") == None

