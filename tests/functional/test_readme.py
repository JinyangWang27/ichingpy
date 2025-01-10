from ichingpy.enum.language import Language
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp


def test_line_interp_display_language_setter():
    assert SixLineLineInterp.display_language == Language.CHINESE
    import ichingpy as icp

    icp.set_language("en")
    assert icp.SixLineLineInterp.display_language == Language.ENGLISH
    icp.set_language("zh")
