from src.fable.generators import NumericGenerator

import pytest


@pytest.fixture
def numeric():
    lower_bound = 0
    upper_bound = 50
    params = dict(lower_bound=lower_bound, upper_bound=upper_bound)
    data = NumericGenerator.generate(20, params)

    return locals()


def test_numeric_return_type(numeric):
    assert isinstance(numeric["data"], list)


def test_numeric_values(numeric):
    for value in numeric["data"]:
        assert value >= numeric["lower_bound"] and value <= numeric["upper_bound"]
