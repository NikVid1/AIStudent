# Base class Vehicle
class Vehicle:
    def __init__(self, make: str, model: str, year: int, price: float):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, price: float, num_doors: int):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price} (Car, {self.num_doors} doors)\n"

class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, price: float, payload_capacity: int):
        super().__init__(make, model, year, price)
        self.payload_capacity = payload_capacity
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price} (Truck, Payload capacity: {self.payload_capacity} kg)\n"

# Inventory list
inventory = [
    Car("Toyota", "Camry", 2023, 24000, 4),
    Truck("Ford", "F-150", 2022, 35000, 1000),
    Car("Honda", "Civic", 2021, 22000, 4)
]

# Display all vehicles and calculate total value
total_value = 0
for vehicle in inventory:
    print(vehicle, end='')
    total_value += vehicle.price

print(f"\nTotal inventory value: ${total_value}")