def test_function_name():
    import numeric_value
    assert hasattr(
        numeric_value, "numeric_value"), "Could not find function numeric_value"


def test_examples():
    from numeric_value import numeric_value
    assert numeric_value("(42)") == -42
    assert numeric_value("42") == 42
