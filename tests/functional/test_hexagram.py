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
