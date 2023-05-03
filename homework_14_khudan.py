class Passenger:
    def __init__(self, name: str, destination: str, place: int):
        self.name = name
        self.destination = destination
        self.place = place

    def __str__(self):
        return f'"name": "{self.name}", "destination": "{self.destination}", "place": {self.place}'


class TrainCar:
    def __init__(self, car_number: int, capacity: int = 10):
        self.car_number = car_number
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger: Passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        else:
            return False

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        passenger_strings = [str(passenger) for passenger in self.passengers]
        passengers = ", ".join(passenger_strings) if passenger_strings else "No passengers"
        return f"Train car number {self.car_number}: {len(self)} passengers - [{passengers}]"


class Train:
    def __init__(self):
        self.cars = []

    def add_car(self, car: TrainCar):
        self.cars.append(car)

    def __len__(self):
        return len(self.cars) - 1

    def __str__(self):
        car_strings = [str(car) for car in self.cars[1:]]
        cars = "\n".join(car_strings) if car_strings else "No cars"
        return f"Train:\n{cars}"

    def add_passenger(self, passenger: Passenger, car_number: int):
        if car_number < len(self.cars):
            if self.cars[car_number].add_passenger(passenger):
                return True
        return False

    def count_passengers(self):
        total_passengers = sum(len(car) for car in self.cars[1:])
        return total_passengers

    def __len__(self):
        return len(self.cars) - 1

    def __str__(self):
        car_strings = [str(car) for car in self.cars[1:]]
        cars = "\n".join(car_strings) if car_strings else "No cars"
        return f"Train:\n{cars}"


passenger1 = Passenger("John Dow", "Name of station", 9)
passenger2 = Passenger("Jane Dow", "Another station", 3)

car1 = TrainCar(1)
car1.add_passenger(passenger1)
car1.add_passenger(passenger2)

car2 = TrainCar(2)
car2.add_passenger(passenger2)

train = Train()
train.add_car(TrainCar(0))  # locomotive
train.add_car(car1)
train.add_car(car2)

print(len(train))  # expected output: 2
print(train.count_passengers())  # expected output: 3

for car in train.cars[1:]:
    print(f"Passengers in train car number {car.car_number}:")
    for passenger in car.passengers:
        print(f"\t{passenger}")
