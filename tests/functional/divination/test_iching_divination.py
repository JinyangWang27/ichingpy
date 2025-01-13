from itertools import product

import pytest


@pytest.mark.parametrize("hexagram_int", product([0, 1], repeat=6))
def test_all_hexagram_exist(hexagram_int: list[int]): ...
