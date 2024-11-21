class CarPark:
    def __init__(self, location = "Unknown", capacity = 100, plates = None, sensors = None, displays = None):
        self.location = location or []
        self.capacity = capacity or []
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        print(f"The location is {self.location} and the current capacity is {self.capacity}]")