#!/usr/bin/python3


class GardenError(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):

    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):

    def __init__(self, message: str):
        super().__init__(message)


class WaterTank:
    __water_level: int
    __max_water_level: int

    def __init__(self, water_level: int = 0, max_water_level: int = 16):
        self.set_max_water_level(max_water_level)
        self.set_water_level(water_level)

    def get_water_level(self) -> int:
        return self.__water_level

    def get_max_water_level(self) -> int:
        return self.__max_water_level

    def set_water_level(self, water_level: int) -> None:
        """
        Set the water tank's current water level after validation.

        Raises:
            GardenError: If water_level is not an integer, is negative,
                or exceeds the maximum allowed water level.
        """
        if not isinstance(water_level, int):
            raise GardenError("Error: water level must be a number")
        if water_level < 0:
            raise GardenError("Error: empty garden water tank")
        if water_level > self.get_max_water_level():
            raise GardenError(
                f"Error: water level {water_level} too high"
                + f" (max {self.get_max_water_level()})")
        self.__water_level = water_level

    def set_max_water_level(self, max_water_level: int) -> None:
        """
        Set the water tank's maximum water level after validation.

        Raises:
            GardenError: If max_water_level is not an integer or is negative.
        """
        if not isinstance(max_water_level, int):
            raise GardenError("Error: max water level must be a number")
        if max_water_level < 0:
            raise GardenError("Error: max water level must be positive")
        self.__max_water_level = max_water_level

    def add_water(self, amount: int) -> None:
        """
        Add water to the tank.

        Raises:
            GardenError: If the resulting water level exceeds the maximum
                or is invalid.
        """
        self.set_water_level(self.get_water_level() + amount)

    def remove_water(self, amount: int) -> None:
        """
        Remove water from the tank.

        Raises:
            GardenError: If the resulting water level becomes negative
                or is invalid.
        """
        self.set_water_level(self.get_water_level() - amount)


class Plant:
    __name: str
    __height: float
    __age: int
    __growth_rate: float
    __water_height: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        gowth_rate: float,
        water_height: int
    ):
        """
        Initialize a Plant instance with validated attributes.

        Raises:
            PlantError: If any of the provided values fail validation
                (invalid name, negative height, negative age, invalid growth
                rate, or negative water height).
        """
        self.set_name(name.capitalize())
        self.set_height(height)
        self.set_age(age)
        self.set_growth_rate(gowth_rate)
        self.set_water_height(water_height)

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_growth_rate(self) -> float:
        return self.__growth_rate

    def get_water_height(self) -> int:
        return self.__water_height

    def set_name(self, name: str) -> None:
        """
        Set the plant's name after validation.

        Raises:
            PlantError: If the name is not a string or is empty.
        """
        GardenSecuritySystem.check_name(name)
        self.__name = name

    def set_height(self, height: float) -> None:
        """
        Set the plant's height after validation.

        Raises:
            PlantError: If height is not a number or is negative.
        """
        GardenSecuritySystem.check_height(height)
        self.__height = height

    def set_age(self, age: int) -> None:
        """
        Set the plant's age after validation.

        Raises:
            PlantError: If age is not an integer or is negative.
        """
        GardenSecuritySystem.check_age(age)
        self.__age = age

    def set_growth_rate(self, growth_rate: float) -> None:
        """
        Set the plant's growth rate after validation.

        Raises:
            PlantError: If growth_rate is not a number or is negative.
        """
        GardenSecuritySystem.check_growth_rate(growth_rate)
        self.__growth_rate = growth_rate

    def set_water_height(self, water_height: int) -> None:
        """
        Set the plant's water height after validation.

        Raises:
            PlantError: If water_height is not an integer or is negative.
        """
        GardenSecuritySystem.check_water_height(water_height)
        self.__water_height = water_height

    def age(self, amount: int = 1) -> None:
        """
        Age the plant by a given amount, triggering growth.

        Raises:
            PlantError: If the resulting height is invalid after growing.
        """
        self.grow(amount)

    def grow(self, amount: int = 1) -> float:
        """
        Increase the plant's height based on its growth rate.

        Raises:
            PlantError: If the resulting height fails validation.
        """
        amount_grown = amount * self.get_growth_rate()
        self.set_height(self.get_height() + amount_grown)
        return amount_grown

    def water(self, water_tank: WaterTank, quantity: int = 1) -> None:
        """
        Increase the plant's water height by the given quantity.

        Raises:
            PlantError: If the resulting water height fails validation
                (e.g. becomes negative).
        """
        water_tank.remove_water(quantity)
        new_water_height = self.get_water_height() + quantity
        self.set_water_height(new_water_height)

    def to_string(self) -> str:
        return (
            f"{self.get_name()} ({self.get_height()}cm, " +
            f"{self.get_age()} days, {self.get_growth_rate()} cm/day)"
        )


class BuggedPlant(Plant):
    """
    Bogus class to test an eventual case were an unhandled exception is raised
    """
    def water(self, _: WaterTank, __: int = 1):
        raise Exception("Error: this plant is bugged lolol")


class GardenSecuritySystem:
    @staticmethod
    def check_name(name: str) -> None:
        """
        Validate a plant name.

        Raises:
            PlantError: If name is not a string or is empty.
        """
        if not isinstance(name, str):
            raise PlantError(f"Error: name {name} must be a string")
        if name == "":
            raise PlantError("Error: name cannot be empty")

    @staticmethod
    def check_height(height: float) -> None:
        """
        Validate a plant height.

        Raises:
            PlantError: If height is not a number or is negative.
        """
        if not (isinstance(height, float) or isinstance(height, int)):
            raise PlantError(f"Error: height {height} must be a number")
        if height < 0:
            raise PlantError(f"Error: height {height} cannot be negative")

    @staticmethod
    def check_age(age: int) -> None:
        """
        Validate a plant age.

        Raises:
            PlantError: If age is not an integer or is negative.
        """
        if not isinstance(age, int):
            raise PlantError(f"Error: age {age} must be a number")
        if age < 0:
            raise PlantError(f"Error: age {age} cannot be negative")

    @staticmethod
    def check_growth_rate(growth_rate: float) -> None:
        """
        Validate a plant growth rate.

        Raises:
            PlantError: If growth_rate is not a number or is negative.
        """
        if (
            not isinstance(growth_rate, float)
            and not isinstance(growth_rate, int)
        ):
            raise PlantError(
                f"Error: growth rate {growth_rate}"
                + " must be a number"
            )
        if growth_rate < 0:
            raise PlantError(
                f"Error: growth rate {growth_rate}"
                + " cannot be negative"
            )

    @staticmethod
    def check_water_height(water_height: int) -> None:
        """
        Validate a plant water height.

        Raises:
            PlantError: If water_height is not an integer or is negative.
        """
        if not isinstance(water_height, int):
            raise PlantError(
                f"Error: water height {water_height}"
                + " must be a number"
            )
        if water_height < 0:
            raise PlantError(
                f"Error: water height {water_height}"
                + " cannot be negative"
            )
        if water_height > 10:
            raise PlantError(
                f"Error: water height {water_height} is too high (max 10)"
            )

    @classmethod
    def check_plant(cls, plant: Plant):
        """
        Validate all attributes of a Plant instance.

        Raises:
            PlantError: If any attribute of the plant fails its validation
                check (name, height, age, growth rate, or water height).
        """
        if plant is None:
            raise PlantError("Error: Plant cannot be None")
        cls.check_name(plant.get_name())
        cls.check_height(plant.get_height())
        cls.check_age(plant.get_age())
        cls.check_growth_rate(plant.get_growth_rate())
        cls.check_water_height(plant.get_water_height())


class Gardener:
    __id: int
    __name: str

    def __init__(self, id: int, name: str):
        self.set_id(id)
        self.set_name(name)

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_id(self, id: int) -> None:
        self.__id = id

    def set_name(self, name: str) -> None:
        self.__name = name


class Garden:
    __gardener: Gardener
    __plants: list[Plant]
    __water_tank: WaterTank
    __total_growth: int

    def __init__(
            self,
            gardener: Gardener,
            plants: list[Plant] | None = None,
            water_tank: WaterTank | None = None
    ):
        self.set_gardener(gardener)
        if plants is None:
            plants = []
        self.set_plants(plants)
        if water_tank is None:
            water_tank = WaterTank()
        self.set_water_tank(water_tank)
        self.set_total_growth(0)

    @staticmethod
    def log(message: str) -> None:
        print(f"[Garden] {message}")

    @classmethod
    def log_error(cls, error: Exception, message: str = "") -> None:
        log_message = ""
        if message is not None and message != "":
            log_message += f"{message}\n"
        log_message += f"{error}"
        cls.log(log_message)

    def get_gardener(self) -> Gardener:
        return self.__gardener

    def set_gardener(self, gardener: Gardener) -> None:
        """
        Set the garden's gardener after validation.

        Raises:
            GardenError: If gardener is None or not an instance of Gardener.
        """
        if gardener is None:
            raise GardenError("Error: gardener cannot be None")
        if not isinstance(gardener, Gardener):
            raise GardenError(
                f"Error: gardener {gardener} must be an instance"
                + "of Gardener"
            )
        self.__gardener = gardener

    def get_plants(self) -> list[Plant]:
        return self.__plants

    def set_plants(self, plants: list[Plant]) -> None:
        if plants is None:
            raise GardenError("Error: plants cannot be None")
        self.__plants = plants

    def get_score(self) -> int:
        return self.__score

    def get_water_tank(self) -> WaterTank:
        return self.__water_tank

    def set_score(self, score: int) -> None:
        self.__score = score

    def get_total_growth(self) -> int:
        return self.__total_growth

    def set_total_growth(self, total_growth: float) -> None:
        """
        Set the garden's total growth value after validation.

        Raises:
            ValueError: If total_growth is not an integer.
        """
        if not isinstance(total_growth, int):
            raise ValueError("Error: total growth must be an integer")
        self.__total_growth = total_growth

    def set_water_tank(self, water_tank: WaterTank) -> None:
        """
        Set the garden's water tank after validation.

        Raises:
            ValueError: If water_tank is None or not an instance of WaterTank.
        """
        if water_tank is None:
            raise ValueError("Error: water tank cannot be None")
        if not isinstance(water_tank, WaterTank):
            raise ValueError(
                "Error: water_tank must be an instance of"
                + " WaterTank"
            )
        self.__water_tank = water_tank

    def add_plant(self, plant: Plant) -> None:
        try:
            GardenSecuritySystem.check_plant(plant)
            self.get_plants().append(plant)
            self.log(
                f"Added {plant.get_name()} to"
                + f" {self.get_gardener().get_name()}'s garden"
            )
        except PlantError as plant_error:
            if plant is not None:
                self.log_error(
                    message=f"PlantError when adding plant {plant.get_name()}"
                    + " to garden:",
                    error=plant_error
                )
            else:
                self.log_error(
                    message="PlantError when adding plant [None]:",
                    error=plant_error
                )
        except GardenError as garden_error:
            self.log_error(
                message="A GardenError occured when adding plant" +
                f"{plant.get_name()} to garden:",
                error=garden_error
            )

    def remove_plant(self, plant: Plant) -> None:
        self.get_plants().remove(plant)

    def fill_water_tank(self):
        """
        Fill the water tank to its maximum level.

        Raises:
            GardenError: If setting the water level fails (e.g. max level
                not set or invalid).
        """
        water_tank = self.get_water_tank()
        water_tank.set_water_level(water_tank.get_max_water_level())

    def grow_all(self) -> None:
        """
        Grow all plants in the garden by one growth cycle.

        Raises:
            ValueError: If updating the total growth value fails.
            PlantError: If any plant's new height fails validation.
        """
        total_growth = 0.0

        for plant in self.get_plants():
            total_growth += plant.grow()
            print(
                f"{plant.get_name().capitalize()}",
                f"grew {plant.get_growth_rate()}cm"
            )
        self.set_total_growth(self.get_total_growth() + total_growth)

    def water_all(self):
        """
        Water all plants in the garden.

        Raises:
            ValueError: If the plants list contains None
            WaterError: Re-raises any WaterError agter logging it.
            GardenError: Re-raises any GardenError agter logging it.
            Exception: Re-raises any exception after logging it.
        """
        for plant in self.get_plants():
            try:
                if plant is None:
                    raise ValueError(
                        "Error: cannot water a plant that is None"
                    )
                plant.water(self.get_water_tank())
                self.log(f"Watering {plant.get_name()} - success")
            except WaterError as water_error:
                self.log_error(
                    message="A water error occured while watering plant"
                    + f" {plant.get_name()}",
                    error=water_error
                )
                raise water_error
            except GardenError as garden_error:
                self.log_error(
                    message="A garden error occured while watering plant"
                    + f" {plant.get_name()}",
                    error=garden_error
                )
                raise garden_error
            except Exception as err:
                log_message = "An error occured while watering plant"
                if plant is not None:
                    log_message += f" {plant.get_name()}"
                else:
                    log_message += "[None]"
                self.log(log_message)
                raise err


class GardenManager:
    # Dict of gardens with their gardeners id as keys
    __gardens: dict[int, list[Garden]]

    def __init__(self, gardens: dict[int, list[Garden]] | None = None):
        if gardens is None:
            gardens = {}
        self.__gardens = gardens

    def log(self, message: str) -> None:
        print(f"[GardenManager] {message}")

    def log_error(cls, error: Exception, message: str = "") -> None:
        log_message = ""
        if message is not None and message != "":
            log_message += f"{message}\n"
        log_message += f"{error}"
        cls.log(log_message)

    def get_gardens(self) -> dict[int, list[Garden]]:
        return self.__gardens

    def create_garden(self, gardener_id: int, gardener_name: str) -> Garden:
        """
        Create a new garden for a gardener and register it.

        Raises:
            GardenError: If the garden is already managed.
        """
        garden = Garden(Gardener(gardener_id, gardener_name))
        self.add_garden(garden)
        return garden

    def __garden_is_managed(self, garden: Garden) -> bool:
        for _, managed_gardens in self.get_gardens().items():
            if garden in managed_gardens:
                return True
        return False

    def add_garden(self, garden: Garden) -> None:
        """
        Register a garden in the manager.

        Raises:
            GardenError: If the garden is already managed.
        """
        if not garden.get_gardener().get_id() in self.get_gardens().keys():
            self.get_gardens()[garden.get_gardener().get_id()] = []
        if not self.__garden_is_managed(garden):
            self.get_gardens()[garden.get_gardener().get_id()].append(garden)
        else:
            raise GardenError("Error: garden is already managed")

    def remove_garden(self, garden: Garden) -> None:
        if self.__garden_is_managed(garden):
            self.get_gardens()[garden.get_gardener().get_id()].remove(garden)

    def grow_garden(self, garden: Garden) -> None:
        self.log(
            f"{garden.get_gardener().get_name()}" +
            " is helping all plants grow..."
        )
        garden.grow_all()

    def water_garden(self, garden: Garden) -> None:
        self.log("Watering plants...")
        try:
            self.log("Opening water system")
            garden.water_all()
        except GardenError as garden_error:
            self.log_error(
                message="A garden error occured when watering plants:",
                error=garden_error
            )
        finally:
            self.log("Closing watering system (cleanup)")


def main():
    print("=== Garden Management System ===")

    plants_to_add: list[Plant | None] = [
        Plant(
            "Oak Tree",
            564.0,
            48180,
            0.15,
            2
        ),
        Plant(
            "Sunflower",
            56.0,
            12,
            0.6,
            1
        ),
        Plant(
            "Rose",
            23.0,
            32,
            0.2,
            0
        ),
        None,
        Plant(
            "Lily of the valley",
            4.0,
            8,
            0.1,
            2
        ),
    ]
    garden_manager = GardenManager()
    gardener = Gardener(0, "Simard")
    water_tank = WaterTank(max_water_level=8)
    garden = Garden(
        gardener=gardener,
        water_tank=water_tank
    )
    garden_manager.add_garden(garden)
    print("\nAdding plants to garden...")
    for plant in plants_to_add:
        garden.add_plant(plant)

    print("\nWatering plants...")
    garden_manager.water_garden(garden)
    print("\nTrying to water plants with an empty water tank...")
    garden.get_water_tank().set_water_level(0)
    garden_manager.water_garden(garden)

    print("\nChecking plant health...")
    valid_plant: Plant
    invalid_plant: Plant
    try:
        valid_plant = Plant("Tomato", 4, 5, 1, 8)
        print(
            f"{valid_plant.get_name()}: healthy (water:" +
            f" {valid_plant.get_water_height()})"
        )
        invalid_plant = Plant("Lettuce", 4, 3, 1, 42)
        print(
            f"{invalid_plant.get_name()}: healthy (water:" +
            f" {invalid_plant.get_water_height()})"
        )
    except PlantError as plant_error:
        print(plant_error)

    print("\nTesting error recovery...")
    try:
        water_tank.set_water_level(-1)
    except GardenError as garden_error:
        print(f"Caught garden error: {garden_error}")
    print("System recovered and continuing...")

    print("\nGarden management system test complete !")


if __name__ == "__main__":
    main()
