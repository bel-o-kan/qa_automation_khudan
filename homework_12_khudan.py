from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def move(self, distance: float):
        pass

class Car(Transport):
    def __init__(self, make: str, model: str, color: str, doors: int):
        self.make = make
        self.model = model
        self.color = color
        self.doors = doors
        self.engine_on = False

    def start(self):
        if not self.engine_on:
            print("Starting the engine...")
            self.engine_on = True
        else:
            print("Engine is already on.")

    def stop(self):
        if self.engine_on:
            print("Stopping the engine...")
            self.engine_on = False
        else:
            print("Engine is already off.")

    def move(self, distance: float):
        if self.engine_on:
            print(f"Moving the car {distance} kilometers...")
        else:
            print("Cannot move the car, engine is off.")


car = Car("Toyota", "Corolla", "white", 4)
car.start()
car.move(12)
car.stop()
