# Creating a base class
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        """
        Constructor to initialize the smartphone's attributes.
        """
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_capacity = battery_capacity

    def display_info(self):
        """
        Method to display smartphone information.
        """
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery: {self.battery_capacity}mAh"

    def charge(self):
        """
        Simulate charging the phone.
        """
        return f"{self.model} is charging..."

# Adding inheritance layer
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, cooling_system):
        """
        Constructor to initialize the gaming smartphone attributes.
        """
        super().__init__(brand, model, storage, battery_capacity)  # Call the parent class constructor
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        """
        Method specific to gaming smartphones.
        """
        return f"Playing {game_name} with {self.cooling_system} cooling system."

# Instantiating objects and using the methods
# Create a regular smartphone
smartphone = Smartphone("Apple", "iPhone 14", 256, 3200)
print(smartphone.display_info())
print(smartphone.charge())

# Create a gaming smartphone
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 512, 6000, "Vapor Chamber")
print(gaming_phone.display_info())
print(gaming_phone.play_game("Genshin Impact"))
