from ichingpy.enum.seasonal_strength import SeasonalStrength


class TestSeasonalStrengthMembers:
    def test_prosperous(self):
        assert SeasonalStrength.PROSPEROUS.value == 1
        assert SeasonalStrength.PROSPEROUS.label == "旺"

    def test_strong(self):
        assert SeasonalStrength.STRONG.value == 2
        assert SeasonalStrength.STRONG.label == "相"

    def test_resting(self):
        assert SeasonalStrength.RESTING.value == 3
        assert SeasonalStrength.RESTING.label == "休"

    def test_imprisoned(self):
        assert SeasonalStrength.IMPRISONED.value == 4
        assert SeasonalStrength.IMPRISONED.label == "囚"

    def test_dead(self):
        assert SeasonalStrength.DEAD.value == 5
        assert SeasonalStrength.DEAD.label == "死"
