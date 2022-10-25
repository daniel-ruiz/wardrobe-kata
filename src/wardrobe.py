from dataclasses import dataclass

@dataclass
class Wall:
    width: int = 0


@dataclass
class Module:
    width: int = 0


def find_wardrobe_combinations(wall, available_modules):
    wardrobe_combinations = []

    _find_module_combinations_recursively(wardrobe_combinations, wall, available_modules)

    return wardrobe_combinations


def _find_module_combinations_recursively(wardrobe_combinations, wall, available_modules):

    for module in available_modules:
        new_combination = [module]
        if _can_find_next_combination(new_combination, wall, available_modules):
            wardrobe_combinations.append(new_combination)


def _can_find_next_combination(current_combination, wall, available_modules):

    if not _does_combination_fit_in_the_wall(current_combination, wall):
        return False

    if (
        _does_combination_fit_in_the_wall(current_combination, wall)
        and _does_combination_fill_the_wall(current_combination, wall, available_modules)
    ):
        return True

    for module in available_modules:
        current_combination.append(module)

        if _can_find_next_combination(current_combination, wall, available_modules):
            return True

        current_combination.pop()

    return False


def _does_combination_fill_the_wall(combination, wall, available_modules):
    return not any(_does_module_fit_in_the_combination(module, combination, wall) for module in available_modules)


def _does_combination_fit_in_the_wall(combination, wall):
    return sum(module.width for module in combination) <= wall.width


def _does_module_fit_in_the_combination(module, combination, wall):
    return module.width + sum(module.width for module in combination) <= wall.width
