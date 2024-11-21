from sensor import Sensor
from display import Display


class CarPark:
    # initializing CarPark class
    def __init__(self, location = "Unknown", capacity = 100, plates = None, sensors = None, displays = None):
        self.location = location or []
        self.capacity = capacity or []
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []


    def __str__(self):
        print(f"The location is {self.location} and the current capacity is {self.capacity}]")

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Type must be either Sensor or Display")

        # Add Sensor to sensors
        if isinstance(component, Sensor):
            self.sensors.append(component)

        # Add Display to displays
        elif isinstance(component, Display):
            self.displays.append(component)

    # add Plate number to plates list
    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    # remove Plate number from plates list
    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        if(self.capacity - len(self.plates)) >= 0:
            return self.capacity - len(self.plates)
        elif(self.capacity - len(self.plates)) < 0:
            return 0

    def update_displays(self):
        # dictionary to send information to the displays
        data = {"available_bays": self.available_bays,
                "temperature": 25}
        for display in self.displays:
            display.update(data)
