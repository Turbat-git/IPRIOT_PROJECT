from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

car_park_instance = CarPark("Moondalup", 100, [], [], [], "moondalup.txt")
entry_sensor = EntrySensor(1, True, car_park_instance)
exit_sensor = ExitSensor(2, True, car_park_instance)

display_instance = Display(1, "Welcome to Moondalup", True, car_park_instance)

if __name__ == "__main__":

    entry_sensor.update_car_park("Test-991")

    for i in range(10):
        entry_sensor.update_car_park(f"Test-{i}")

    for i in range(2):
        exit_sensor.update_car_park(f"Test-{i}")