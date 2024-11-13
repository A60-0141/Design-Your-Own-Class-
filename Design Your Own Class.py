# Smartphone and Polymorphism Challenge in one file

# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")


# Inherited Class: SmartphoneWithCamera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, camera_quality):
        super().__init__(brand, model, price)  # Initialize parent class
        self.camera_quality = camera_quality

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} camera!")


# Base Class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Derived Class: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


# Derived Class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# Derived Class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")


# Main Code Execution
smartphone = SmartphoneWithCamera("Apple", "iPhone 14", 999, "12 MP")
smartphone.display_info()
smartphone.make_call("123-456-7890")
smartphone.send_message("123-456-7890", "Hello!")
smartphone.take_photo()

# Create instances of vehicles
car = Car()
plane = Plane()
bicycle = Bicycle()

# Call the move() method on each instance
car.move()
plane.move()
bicycle.move()
