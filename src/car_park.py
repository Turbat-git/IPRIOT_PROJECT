from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime


class CarPark:
    # initializing CarPark class
    def __init__(self, location = "Unknown", capacity = 100, plates = None, sensors = None, displays = None, log_file = Path("log.txt")):
        self.location = location or []
        self.capacity = capacity or []
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

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
        self.log_car_activity(plate, "entered")

    # remove Plate number from plates list
    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self.log_car_activity(plate, "exited")

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

    def log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

