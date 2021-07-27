import pytest

from chops.hex_to_int import hex_to_int


@pytest.mark.parametrize("value", ["5a", "6B", "ff", "1", "7aB2f"])
def test_hex_to_int(value):
    assert hex_to_int(value) == int(value, 16)
