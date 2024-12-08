# Creating a base class
class Vehicle:
    def move(self):
        """
        Generic method to describe movement.
        """
        return "This vehicle moves in its own way."

# Defining specific vehicle classes with unique move() methods
class Car(Vehicle):
    def move(self):
        return "The car drives on roads. 🚗"

class Plane(Vehicle):
    def move(self):
        return "The plane flies in the sky. ✈️"

class Boat(Vehicle):
    def move(self):
        return "The boat sails on water. 🚤"

# Demonstrate polymorphism
# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Iterate through the list and call the move() method
for vehicle in vehicles:
    print(vehicle.move())
