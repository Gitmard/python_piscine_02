#!/usr/bin/python3

class Plant:
    __name: str

    def __init__(self, name: str):
        self.set_name(name)

    def water(self):
        print(f"Watering {self.get_name()}")

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name


def water_plants(plants_list: list[Plant]) -> bool:
    success = False

    print("Opening watering system")
    try:
        for plant in plants_list:
            if plant is None:
                raise Exception("Cannot water None - invalid plant!")
            plant.water()
        success = True
    except Exception as err:
        print(f"Error: {err}")
    finally:
        print("Closing watering system (cleanup)")
    return success


def test_watering_system():
    good_list = [
        Plant("tomato"),
        Plant("lettuce"),
        Plant("carrots")
    ]
    faulty_list = [
        Plant("tomato"),
        None,
        Plant("carrots")
    ]

    print("\nTesting normal watering...")
    if water_plants(good_list):
        print("Watering completed successfully!")

    print("\nTesting with error...")
    if water_plants(faulty_list):
        print("Watering completed successfully!")

    print("\nCleanup always happens, even with errors!")


def main():
    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()
