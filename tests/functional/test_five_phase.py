from ichingpy.enum.five_phase import FivePhase


def test_five_phase_generates():
    assert FivePhase.METAL.generates == FivePhase.WATER
    assert FivePhase.WATER.generates == FivePhase.WOOD
    assert FivePhase.WOOD.generates == FivePhase.FIRE
    assert FivePhase.FIRE.generates == FivePhase.EARTH
    assert FivePhase.EARTH.generates == FivePhase.METAL


def test_five_phase_generated_by():
    assert FivePhase.METAL.generated_by == FivePhase.EARTH
    assert FivePhase.WATER.generated_by == FivePhase.METAL
    assert FivePhase.WOOD.generated_by == FivePhase.WATER
    assert FivePhase.FIRE.generated_by == FivePhase.WOOD
    assert FivePhase.EARTH.generated_by == FivePhase.FIRE


def test_five_phase_overcomes():
    assert FivePhase.METAL.overcomes == FivePhase.WOOD
    assert FivePhase.WOOD.overcomes == FivePhase.EARTH
    assert FivePhase.EARTH.overcomes == FivePhase.WATER
    assert FivePhase.WATER.overcomes == FivePhase.FIRE
    assert FivePhase.FIRE.overcomes == FivePhase.METAL


def test_five_phase_overcome_by():
    assert FivePhase.METAL.overcome_by == FivePhase.FIRE
    assert FivePhase.WOOD.overcome_by == FivePhase.METAL
    assert FivePhase.EARTH.overcome_by == FivePhase.WOOD
    assert FivePhase.WATER.overcome_by == FivePhase.EARTH
    assert FivePhase.FIRE.overcome_by == FivePhase.WATER
