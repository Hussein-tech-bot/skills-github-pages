# =========================================
# OOP Master Program 🏗️ Polymorphism & Encapsulation
# Author: Wangui

# =========================================

# ------------------------
# Part 1: Devices & Smartphones
# ------------------------

# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Subclass: Smartphone inherits from Device
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.__os = os  # private attribute
        self.storage = storage

    # Getter for encapsulated attribute
    def get_os(self):
        return self.__os

    # Method to simulate a call
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")


# ------------------------
# Part 2: Vehicles & Polymorphism
# ------------------------

# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # generic method to be overridden


# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛴️")


# ------------------------
# Main Program
# ------------------------
def main():
    print("\n=== Device & Smartphone Demo ===")
    phone1 = Smartphone("Apple", "iPhone 14", "iOS 17", "128GB")
    phone2 = Smartphone("Samsung", "Galaxy S23", "Android 14", "256GB")

    print(phone1.device_info())
    print("Operating System:", phone1.get_os())
    phone1.make_call("0712345678")

    print(phone2.device_info())
    print("Operating System:", phone2.get_os())
    phone2.make_call("0798765432")

    print("\n=== Vehicle Polymorphism Demo ===")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()


if __name__ == "__main__":
    main()
