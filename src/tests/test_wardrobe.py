import pytest

from wardrobe import find_wardrobe_combinations, Wall, Module


@pytest.mark.parametrize(('wall', 'expected_combinations'), [
    (Wall(width=250), [[Module(width=50), Module(width=50), Module(width=50), Module(width=50), Module(width=50)]]),
    (Wall(width=150), [[Module(width=50), Module(width=50), Module(width=50)]]),
    (Wall(width=100), [[Module(width=50), Module(width=50)]]),
])
def test_wall_is_filled_with_modules_of_the_same_type(wall, expected_combinations):
    combinations = find_wardrobe_combinations(wall=wall, available_modules=[Module(width=50)])

    assert combinations == expected_combinations


def test_wall_is_filled_with_two_types_of_module():
    combinations = find_wardrobe_combinations(wall=Wall(width=75), available_modules=[Module(width=50), Module(width=25)])

    assert combinations == [
        [Module(width=50), Module(width=25)],
        [Module(width=25), Module(width=50)],
        [Module(width=25), Module(width=25), Module(width=25)],
    ]
