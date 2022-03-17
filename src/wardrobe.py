from dataclasses import dataclass

@dataclass
class Wall:
    width: int = 0


@dataclass
class Module:
    width: int = 0


def find_wardrobe_combinations(wall, available_modules, combinations=None):
    module = available_modules[0]

    if combinations is None:
        first_combination = []
        return find_wardrobe_combinations(wall, available_modules, combinations=[first_combination])

    combination = combinations[0]

    if _does_module_fit_in_wall(module, wall):
        combination.append(module)
        remaining_width = wall.width - module.width
        remaining_wall = Wall(width=remaining_width)
        return find_wardrobe_combinations(remaining_wall, available_modules, combinations)

    return combinations


def _does_module_fit_in_wall(module, wall):
    return module.width <= wall.width
