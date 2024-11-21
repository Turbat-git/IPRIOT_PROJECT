class Sensor:
    # initializing Sensor class
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        #overriding the public string method
        print(f"{self.id}'s current status is {self.is_active}")

class EntrySensor:
    pass

class ExitSensor:
    pass