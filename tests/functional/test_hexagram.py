from datetime import datetime

from ichingpy.model.hexagram import Hexagram


def test_hexagram_correct_range_of_line_number():
    results: list[int] = []
    for _ in range(1000):
        yu_ce_1 = Hexagram.bian(49)
        yu_ce_2 = Hexagram.bian(yu_ce_1)
        yu_ce_3 = Hexagram.bian(yu_ce_2)
        results.append(yu_ce_3 // 4)
    assert max(results) == 9
    assert min(results) == 6


def test_hexagram_from_datetime():
    dt = datetime(2022, 3, 31, 11, 0, 0)  # 壬寅年 癸卯月 癸未日 戊午时
    hexagram = Hexagram.from_datetime(dt)  # 蒙之未济卦
    assert [line.status.value for line in hexagram.lines] == [2, 1, 2, 0, 2, 1]
