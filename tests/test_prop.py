from src.datarpg import prop


def test_damage_prop_works() -> None:
    assert prop.damage(prop.Prop(), 1) == prop.Prop(health=999)


def test_damage_can_destroy_props() -> None:
    assert prop.damage(prop.Prop(), 1000) == prop.Prop(health=0, is_destroyed=True)


def test_damage_health_never_goes_under_zero() -> None:
    assert prop.damage(prop.Prop(), 2000) == prop.Prop(health=0, is_destroyed=True)
