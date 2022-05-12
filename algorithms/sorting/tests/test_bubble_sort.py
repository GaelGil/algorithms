import pytest
import random
from ..bubble_sort import bubble_sort


@pytest.fixture
def generate_data():
    data =  [random.randint(0, 100) for j in range(100)]
    return data


@pytest.mark.parametrize('n_tests', range(50))
def test_sort(n_tests, generate_data):
    input_ = generate_data
    assert bubble_sort(input_) == sorted(input_)

