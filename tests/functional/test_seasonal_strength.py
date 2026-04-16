from ichingpy.enum.seasonal_strength import SeasonalStrength
from ichingpy.enum.five_phase import FivePhase


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


class TestSeasonalStrengthWoodMonth:
    """All 5 phases in a WOOD month."""

    def test_prosperous(self):
        assert FivePhase.WOOD.seasonal_strength(FivePhase.WOOD) == SeasonalStrength.PROSPEROUS

    def test_strong(self):
        # WOOD generates FIRE → FIRE is STRONG in a WOOD month
        assert FivePhase.FIRE.seasonal_strength(FivePhase.WOOD) == SeasonalStrength.STRONG

    def test_resting(self):
        # WATER generates WOOD → WATER is RESTING in a WOOD month
        assert FivePhase.WATER.seasonal_strength(FivePhase.WOOD) == SeasonalStrength.RESTING

    def test_imprisoned(self):
        # METAL overcomes WOOD → METAL is IMPRISONED in a WOOD month
        assert FivePhase.METAL.seasonal_strength(FivePhase.WOOD) == SeasonalStrength.IMPRISONED

    def test_dead(self):
        # WOOD overcomes EARTH → EARTH is DEAD in a WOOD month
        assert FivePhase.EARTH.seasonal_strength(FivePhase.WOOD) == SeasonalStrength.DEAD


class TestSeasonalStrengthFireMonth:
    """Spot-check FIRE month to verify correctness across months."""

    def test_prosperous(self):
        assert FivePhase.FIRE.seasonal_strength(FivePhase.FIRE) == SeasonalStrength.PROSPEROUS

    def test_strong(self):
        # FIRE generates EARTH → EARTH is STRONG in a FIRE month
        assert FivePhase.EARTH.seasonal_strength(FivePhase.FIRE) == SeasonalStrength.STRONG

    def test_resting(self):
        # WOOD generates FIRE → WOOD is RESTING in a FIRE month
        assert FivePhase.WOOD.seasonal_strength(FivePhase.FIRE) == SeasonalStrength.RESTING

    def test_imprisoned(self):
        # WATER overcomes FIRE → WATER is IMPRISONED in a FIRE month
        assert FivePhase.WATER.seasonal_strength(FivePhase.FIRE) == SeasonalStrength.IMPRISONED

    def test_dead(self):
        # FIRE overcomes METAL → METAL is DEAD in a FIRE month
        assert FivePhase.METAL.seasonal_strength(FivePhase.FIRE) == SeasonalStrength.DEAD


class TestSeasonalStrengthMetalMonth:
    """Spot-check METAL month."""

    def test_prosperous(self):
        assert FivePhase.METAL.seasonal_strength(FivePhase.METAL) == SeasonalStrength.PROSPEROUS

    def test_strong(self):
        # METAL generates WATER → WATER is STRONG
        assert FivePhase.WATER.seasonal_strength(FivePhase.METAL) == SeasonalStrength.STRONG

    def test_resting(self):
        # EARTH generates METAL → EARTH is RESTING
        assert FivePhase.EARTH.seasonal_strength(FivePhase.METAL) == SeasonalStrength.RESTING

    def test_imprisoned(self):
        # FIRE overcomes METAL → FIRE is IMPRISONED
        assert FivePhase.FIRE.seasonal_strength(FivePhase.METAL) == SeasonalStrength.IMPRISONED

    def test_dead(self):
        # METAL overcomes WOOD → WOOD is DEAD
        assert FivePhase.WOOD.seasonal_strength(FivePhase.METAL) == SeasonalStrength.DEAD


class TestSeasonalStrengthPublicImport:
    def test_seasonal_strength_importable_from_enum_package(self):
        from ichingpy.enum import SeasonalStrength
        assert SeasonalStrength.PROSPEROUS.label == "旺"
