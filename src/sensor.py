from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    # initializing Sensor class
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        #overriding the public string method
        print(f"{self.id}'s current status is {self.is_active}")

    #utilize detect_vehicle to update car_park
    @abstractmethod
    def update_car_park(self, plate):
        pass

    #scanning and saving the plate number of scanned plates
    def _scan_plate(self):
        return 'FAKE' + format(random.randint(0, 999), '03d')

    #updating car_park using the scanned plate number
    def detect_vehicle(self):
        plate= self._scan_plate()
        self.update_car_park(plate)

class EntrySensor:
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor:
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate})

    def _scan_plate(self):
        return random.choice(self.car_park.plates)