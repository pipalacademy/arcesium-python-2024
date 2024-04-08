
def test_function_name():
    import reverse_digits
    assert hasattr(
        reverse_digits, "reverse_digits"), "Could not find function reverse_digits"


def test_reverse_digits():
    from reverse_digits import reverse_digits
    assert reverse_digits(1234) == 4321
    assert reverse_digits(3456) == 6543
