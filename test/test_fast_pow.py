from src.fast_pow import fast_pow


def test_two_power_two():
    assert fast_pow(2, 2) == 4


def test_negative_base():
    assert fast_pow(-1, 4) == 1

def test_negative_power_returns_none():
    assert fast_pow(2, -1) is None


def test_zero_power_returns_one():
    assert fast_pow(5, 0) == 1
    assert fast_pow(100, 0) == 1
    assert fast_pow(-3, 0) == 1


def test_power_of_one_returns_same_number():
    assert fast_pow(5, 1) == 5
    assert fast_pow(-3, 1) == -3


def test_zero_base_cases():
    assert fast_pow(0, 1) == 0
    assert fast_pow(0, 5) == 0


def test_float_base():
    assert fast_pow(2.5, 2) == 6.25


def test_non_integer_power_returns_none():
    assert fast_pow(2, 2.5) is None


def test_zero_to_zero_returns_none():
    assert fast_pow(0, 0) is None

