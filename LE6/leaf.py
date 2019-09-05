from Vehicle import Vehicle
from electricpowered import ElectricPowered

class Nissan_Leaf(Vehicle, ElectricPowered):
    def __init__(self, model, manufacturer, horsepower, wheel_count, capacity):
        Vehicle.__init__(self, "Leaf", "Nissan", 50, 4)
        ElectricPowered.__init__(self, 45)

    def drive(self):
        ElectricPowered.drive(self, 1)