# Define the Car class
class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0

    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False
        self.current_speed = 0

    def accelerate(self):
        if self.is_engine_started:
            self.current_speed += self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def apply_brakes(self):
        if self.is_engine_started:
            self.current_speed -= self.tyre_friction
            if self.current_speed < 0:
                self.current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car has not started yet")


# Define the Truck class inheriting from Car
class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self.max_cargo_weight = max_cargo_weight
        self.load = 0  # current load of the truck

    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Car has not started yet")

    def load_cargo(self, cargo_weight):
        if self.is_engine_started:
            print("Cannot load cargo during motion")
        else:
            if cargo_weight > self.max_cargo_weight:
                print(f"Cannot load cargo more than max limit: {self.max_cargo_weight}")
            else:
                self.load += cargo_weight

    def unload_cargo(self, cargo_weight):
        if self.is_engine_started:
            print("Cannot unload cargo during motion")
        else:
            if cargo_weight > self.load:
                self.load = 0
            else:
                self.load -= cargo_weight


# Testing the classes
def default_test():
    # Creating a Truck instance
    truck = Truck("Red", 120, 50, 10, 1000)

    # Initial state assertions
    assert truck.is_engine_started == False
    assert truck.current_speed == 0
    assert truck.load == 0

    # Testing sound_horn method
    truck.sound_horn()  # Output should be "Car has not started yet"
    truck.start_engine()
    truck.sound_horn()  # Output should be "Honk Honk"

    # Testing load_cargo method
    truck.load_cargo(800)  # Truck engine is off, so cargo should load
    assert truck.load == 800
    truck.start_engine()
    truck.load_cargo(500)  # Truck engine is on, so cargo shouldn't load
    assert truck.load == 800  # Should remain 800

    # Testing unload_cargo method
    truck.stop_engine()
    truck.unload_cargo(300)  # Truck engine is off, cargo should unload
    assert truck.load == 500
    truck.start_engine()
    truck.unload_cargo(700)  # Truck engine is on, cargo shouldn't unload
    assert truck.load == 500  # Should remain 500
