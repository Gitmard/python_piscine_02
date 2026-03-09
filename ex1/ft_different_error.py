#!/usr/bin/python3

def garden_operations(error: str) -> None:
    print("\nTesting multiple error together...")
    if error == "value":
        # Imaginary numbers ? Yeah right...
        int("i")
    elif error == "zero_division":
        # Marcel could do it.
        42 / 0
    elif error == "file_not_found":
        # The cake is a lie !
        open("the cake").close()
    elif error == "key_error":
        # Evidently, there is no spoon
        {"not a spoon": "is"}["a spoon"]
    elif error == "all":
        # Random bullshit, go !!
        int("i")
        42 / 0
        open("the cake").close()
        {"not a spoon": "is"}["a spoon"]


def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as value_error:
        print(f"Caught value error: {value_error}")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero_division")
    except ZeroDivisionError as zero_division_error:
        print(f"Caught ZeroDivisionError: {zero_division_error}")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file_not_found")
    except FileNotFoundError as file_not_found_error:
        print(f"Caught FileNotFoundError: {file_not_found_error}")
    print("\nTesting KeyError...")
    try:
        garden_operations("key_error")
    except KeyError as key_error:
        print(f"Caught KeyError: {key_error}")
    try:
        garden_operations("all")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues !")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("\nAll error types tested successfully!")
