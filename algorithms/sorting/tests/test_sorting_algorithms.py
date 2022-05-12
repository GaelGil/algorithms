import pytest
import random
from ..bubble_sort import bubble_sort
from ..merge_sort import merge_sort
from ..selection_sort import selection
# from ..insertion_sort import


@pytest.fixture
def generate_data():
    data =  [random.randint(0, 100) for j in range(100)]
    return data


@pytest.mark.parametrize('n_tests', range(50))
def test_sort(n_tests, generate_data):
    input_ = generate_data
    assert bubble_sort(input_) == sorted(input_)

@pytest.mark.parametrize('n_tests', range(50))
def test_sort(n_tests, generate_data):
    input_ = generate_data
    assert merge_sort(input_) == sorted(input_)

@pytest.mark.parametrize('n_tests', range(50))
def test_sort(n_tests, generate_data):
    input_ = generate_data
    assert selection(input_) == sorted(input_)

# @pytest.mark.parametrize('n_tests', range(50))
# def test_sort(n_tests, generate_data):
#     input_ = generate_data
#     assert bubble_sort(input_) == sorted(input_)

