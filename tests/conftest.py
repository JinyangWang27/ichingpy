import pytest

from ichingpy.divination.six_lines import SixLinesDivinationEngine


@pytest.fixture
def six_line_engine() -> SixLinesDivinationEngine:
    return SixLinesDivinationEngine()
