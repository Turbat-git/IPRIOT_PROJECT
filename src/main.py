from typing import AnyStr

from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

CarPark("Moondalup", 100, AnyStr, None, None, "moondalup.txt")
entry_sensor = EntrySensor(1, True, CarPark)
exit_sensor = ExitSensor(2, True, CarPark)

Display(1, "Welcome to Moondalup", True, CarPark)

entry_sensor.update_car_park("Test-991")

for i in range(10):
    entry_sensor.update_car_park(f"Test-{i}")

for i in range(2):
    exit_sensor.update_car_park(f"Test-{i}")

for i in range(2):
    print(i)


