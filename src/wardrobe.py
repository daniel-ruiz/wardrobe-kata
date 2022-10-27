import contextlib
from copy import copy
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
    modules_to_try = copy(available_modules)
    modules_to_try.reverse()

    module = modules_to_try.pop()
    with contextlib.suppress(IndexError):
        while True:
            new_combination = [module]
            if _can_find_next_combination(new_combination, wall, available_modules, wardrobe_combinations):
                wardrobe_combinations.append(new_combination)
            else:
                module = modules_to_try.pop()


def _can_find_next_combination(current_combination, wall, available_modules, wardrobe_combinations):

    if (
        not _does_combination_fit_in_the_wall(current_combination, wall)
        or _is_combination_already_found(current_combination, wardrobe_combinations)
    ):
        return False

    if (
        _does_combination_fit_in_the_wall(current_combination, wall)
        and _does_combination_fill_the_wall(current_combination, wall, available_modules)
    ):
        return True

    for module in available_modules:
        current_combination.append(module)

        if _can_find_next_combination(current_combination, wall, available_modules, wardrobe_combinations):
            return True

        current_combination.pop()

    return False


def _does_combination_fill_the_wall(combination, wall, available_modules):
    return not any(_does_module_fit_in_the_combination(module, combination, wall) for module in available_modules)


def _does_combination_fit_in_the_wall(combination, wall):
    return sum(module.width for module in combination) <= wall.width


def _does_module_fit_in_the_combination(module, combination, wall):
    return module.width + sum(module.width for module in combination) <= wall.width


def _is_combination_already_found(combination, found_combinations):
    return any(_are_combinations_equal(combination, found_combination) for found_combination in found_combinations)


def _are_combinations_equal(combination, other_combination):
    return (
        len(combination) == len(other_combination)
        and all(module in other_combination for module in combination)
        and all(other_module in combination for other_module in other_combination)
    )
