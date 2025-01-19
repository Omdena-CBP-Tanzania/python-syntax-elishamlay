import pytest
from assignment import *

def test_format_string():
    assert format_string("Alice", 30) == "My name is Alice and I am 30 years old"

def test_conditional_check():
    assert conditional_check(15) == "Greater"
    assert conditional_check(5) == "Lesser"
    assert conditional_check(10) == "Equal"

def test_loop_sum():
    assert loop_sum(5) == 15  # 1 + 2 + 3 + 4 + 5

def test_list_operations():
    assert list_operations([1, 2, 3, 4, 5]) == (15, 5, 1)

def test_dict_operations():
    assert dict_operations({"Alice": 85, "Bob": 75, "Charlie": 90}) == ["Alice", "Charlie"]

def test_set_operations():
    assert set_operations([1, 2, 3], [2, 3, 4]) == {2, 3}

def test_arithmetic_ops():
    assert arithmetic_ops(10, 5) == {
        'sum': 15,
        'difference': 5,
        'product': 50,
        'quotient': 2.0
    }

def test_logical_ops():
    assert logical_ops(True, False) == {
        'and': False,
        'or': True,
        'not_x': False
    }

def test_bitwise_ops():
    assert bitwise_ops(5, 3) == {
        'and': 1,
        'or': 7,
        'xor': 6
    }
