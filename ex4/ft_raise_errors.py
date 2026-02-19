#!/usr/bin/python3

def check_plant_name(name: str) -> None:
    if not isinstance(name, str):
        raise ValueError(
            f"Error: Name {name}"
            + " must be a string")
    if len(name) == 0:
        raise ValueError("Error: Plant name cannot be empty!")


def check_water_level(water_level: int) -> bool:
    if not isinstance(water_level, int):
        raise ValueError(
            f"Error: Water level {water_level}"
            + " must be an int")
    if water_level < 1:
        raise ValueError(
            f"Error: Water level {water_level}"
            + " is too low (min 1)"
        )
    elif water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level}"
            + " is too high (max 10)"
        )


def check_sunlight_hours(sunlight_hours: int) -> bool:
    if not isinstance(sunlight_hours, int):
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours}"
            + " must be an int")
    if sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours}"
            + " is too low (min 2)"
        )
    elif sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours}"
            + " is too high (max 12)"
        )


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    check_plant_name(plant_name)
    check_water_level(water_level)
    check_sunlight_hours(sunlight_hours)


def test_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    try:
        check_plant_health(plant_name, water_level, sunlight_hours)
    except ValueError as error:
        print(error)
    except Exception as err:
        print(err)
        raise err


def main():
    plant_name = "tomato"
    water_level = 6
    sunlight_hours = 10

    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    test_plant_health(plant_name, water_level, sunlight_hours)

    print("\nTesting empty plant name...")
    plant_name = ""
    test_plant_health(plant_name, water_level, sunlight_hours)

    print("\nTesting bad water level...")
    plant_name = "tomato"
    water_level = 42
    test_plant_health(plant_name, water_level, sunlight_hours)

    print("\nTesting bad sunlight hours...")
    water_level = 6
    sunlight_hours = 1
    test_plant_health(plant_name, water_level, sunlight_hours)

    print("\nTesting bad name type")
    plant_name = 42
    sunlight_hours = 10
    test_plant_health(plant_name, water_level, sunlight_hours)

    print("\nAll raising tests completed!")


if __name__ == "__main__":
    main()
