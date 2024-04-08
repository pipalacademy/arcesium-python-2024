import pytest


def test_function_name():
    import simple_interest
    assert hasattr(
        simple_interest, "simple_interest"), "Could not find function simple_interest"


def test_simple_interest():
    from simple_interest import simple_interest
    assert simple_interest(10000, 8, 5) == pytest.approx(4000.0)
    assert simple_interest(100, 4, 1) == pytest.approx(4.0)
