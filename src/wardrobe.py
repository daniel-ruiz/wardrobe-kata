from dataclasses import dataclass

@dataclass
class Wall:
    width: int = 0


@dataclass
class Module:
    width: int = 0


def find_wardrobe_combinations(wall, available_modules):
    module = available_modules[0]
    first_combination = []

    remaining_wall = wall
    while _does_module_fit_in_wall(module, remaining_wall):
        first_combination.append(module)
        remaining_width = remaining_wall.width - module.width
        remaining_wall = Wall(width=remaining_width)

    return [first_combination]


def _does_module_fit_in_wall(module, wall):
    return module.width <= wall.width
