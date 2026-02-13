#!/usr/bin/python3

class GardenError(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):

    def __init__(self, name: str):
        super().__init__(f"The {name} plant is wilting!")


class WaterError(GardenError):

    def __init__(self):
        super().__init__("Not enough water in the tank!")


def test_plant_error():
    raise PlantError("tomato")


def test_water_error():
    raise WaterError()


def main():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        test_plant_error()
    except PlantError as garden_error:
        print(f"Caught PlantError: {garden_error}")

    print("\nTesting WaterError...")
    try:
        test_water_error()
    except WaterError as water_error:
        print(f"Caught WaterError: {water_error}")

    print("\nTesting catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as garden_error:
        print(f"Caught a garden error: {garden_error}")
    try:
        test_water_error()
    except GardenError as garden_error:
        print(f"Caught a garden error: {garden_error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
