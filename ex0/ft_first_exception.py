#!/usr/bin/python3

def check_temperature(temp_str: str) -> int | None:
    temp_int: int | None = None
    try:
        temp_int = int(temp_str)
        if 0 <= temp_int <= 40:
            print(f"Temperature {temp_str}°C is perfect for plants!")
        else:
            if temp_int < 0:
                print(
                    f"Error: Temperature {temp_str}°C is too cold for plants",
                    "(min 0°C)")
            else:
                print(
                    f"Error: Temperature {temp_str}°C is too hot for plants",
                    "(max 40°C)")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
    except Exception as err:
        print(f"Error: Unknown exception: {err}")
        raise err
    return temp_int


def test_temperature_input() -> None:
    temp_str = "invalid"
    print(f"\nTesting temperature: {temp_str}")
    check_temperature(temp_str)
    print("")
    temp_str = "-100"
    check_temperature(temp_str)
    print("")
    temp_str = "100"
    check_temperature(temp_str)
    print("")
    temp_str = "25"
    check_temperature(temp_str)
    print("")
    temp_str = "0"
    check_temperature(temp_str)
    print("")
    temp_str = "40"
    check_temperature(temp_str)
    print("")
    check_temperature("254325482435762837456283746528943576")
    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    test_temperature_input()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("An unknown error occured, exiting...")
