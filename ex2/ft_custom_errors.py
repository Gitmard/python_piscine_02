#!/usr/bin/python3

class GardenError(Exception):
    pass


class PlantError(GardenError):

    def __init__(self, name: str) -> None:
        super().__init__(f"The {name} plant is wilting!")


class WaterError(GardenError):

    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError("tomato")
    except PlantError as garden_error:
        print(f"Caught PlantError: {garden_error}")

    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as water_error:
        print(f"Caught WaterError: {water_error}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("tomato")
    except GardenError as garden_error:
        print(f"Caught a garden error: {garden_error}")
    try:
        raise WaterError()
    except GardenError as garden_error:
        print(f"Caught a garden error: {garden_error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
