# import unittest
import pytest
import random
from ..bubble_sort import bubble_sort

test_data = []

def generate_data(num_lists):
    data = []
    for i in range(num_lists):
        current_list =  [random.randint(0, 100) for j in range(100)]
        data.append(current_list)
    return data

# print(generate_data(num_lists=5))

test_data = generate_data(10)

# print(sorted(test_data[0]))

# @pytest.mark.parametrize("a,b,expected", test_data)
@pytest.mark.parametrize('non_sorted', [non_sorted])
def test_sort(non_sorted):
    assert bubble_sort(non_sorted) == sorted(non_sorted)

for i in test_data:
    test_sort(i)