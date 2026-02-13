#!/usr/bin/python3

def test_value_error():
    # Imaginary numbers ? Yeah right...
    return int("i")


def test_zero_division_error():
    # Marcel could do it.
    return 42 / 0


def test_file_not_found_error():
    # The cake is a lie !
    open("the cake").close()


def test_key_error():
    # Evidently, there is no spoon
    return {"not a spoon": "is"}["a spoon"]


def test_error_types():
    print("\nTesting multiple error together...")
    try:
        test_value_error()
        test_zero_division_error()
        test_file_not_found_error()
        test_key_error()
    except Exception:
        print("Caught an error. but program continues!")


def garden_operations():
    print("Testing ValueError...")
    try:
        test_value_error()
    except ValueError as value_error:
        print(f"Caught value error: {value_error}")
    print("\nTesting ZeroDivisionError...")
    try:
        test_zero_division_error()
    except ZeroDivisionError as zero_division_error:
        print(f"Caught ZeroDivisionError: {zero_division_error}")
    print("\nTesting FileNotFoundError...")
    try:
        test_file_not_found_error()
    except FileNotFoundError as file_not_found_error:
        print(f"Caught FileNotFoundError: {file_not_found_error}")
    print("\nTesting KeyError...")
    try:
        test_key_error()
    except KeyError as key_error:
        print(f"Caught KeyError: {key_error}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    test_error_types()
    print("\nAll error types tested successfully!")
