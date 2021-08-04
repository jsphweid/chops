import pytest

from chops.swap_endian import swap_endian, swap_endian2

test_cases = [
    ("feff", "fffe"),
    ("1234", "3412"),
    ("11223344", "44332211"),
]


@pytest.mark.parametrize("value, result", test_cases)
def test_swap_endian(value, result):
    assert swap_endian(value) == result


@pytest.mark.parametrize("value, result", test_cases)
def test_swap_endian2(value, result):
    assert swap_endian2(value) == result
