from wardrobe import find_wardrobe_combinations, Wall, Module


def test_wall_is_filled_with_modules_of_the_same_type():
    combinations = find_wardrobe_combinations(wall=Wall(width=250), available_modules=[Module(width=50)])

    assert combinations == [
        [Module(width=50), Module(width=50), Module(width=50), Module(width=50), Module(width=50)],
    ]
