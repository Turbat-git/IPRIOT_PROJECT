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
    
    