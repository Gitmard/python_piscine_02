#!/usr/bin/python3

def check_temperature(temp_str):
    temp_int: int
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
        if 0 <= temp_int <= 40:
            print(f"Temperature {temp_str}°C is perfect for plants!")
        else:
            if temp_int < 0:
                print(
                    f"Temperature {temp_str}°C is too cold for plants",
                    "(min 0°C)")
            else:
                print(
                    f"Temperature {temp_str}°C is too hot for plants",
                    "(max 40°C)")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")


def main():
    print("=== Garden Temperature Checker ===")
    check_temperature("invalid")
    print("")
    check_temperature("-100")
    print("")
    check_temperature("100")
    print("")
    check_temperature("25")
    print("")
    check_temperature("0")
    print("")
    check_temperature("40")
    print("")
    check_temperature("254325482435762837456283746528943576")


if __name__ == "__main__":
    main()
