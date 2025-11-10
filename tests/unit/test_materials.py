from generators.core.utils.materials import STANDARD_MATERIALS, Material, get_material


def test_get_material_returns_known_material():
    material = get_material("PLA+")
    assert isinstance(material, Material)
    assert material == STANDARD_MATERIALS["PLA+"]


def test_get_material_raises_value_error_for_unknown_name():
    message = "Unknown material: unobtanium"
    try:
        get_material("unobtanium")
    except ValueError as exc:  # pragma: no cover - defensive guard
        assert str(exc) == message
    else:  # pragma: no cover - defensive guard
        raise AssertionError("ValueError not raised")
