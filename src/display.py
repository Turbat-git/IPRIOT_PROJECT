class Display:
    def __init__(self, id, message = "Welcome to the car park", is_on = None, car_park = None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        print(f"Display {self.id}: {self.message}")

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")

        if "id" in data:
            self.id = data["id"]
        if "message" in data:
            self.message= data["message"]
        if "is_on" in data:
            self.is_on = data["is_on"]
        if "car_park" in data:
            self.car_park = data["car_park"]