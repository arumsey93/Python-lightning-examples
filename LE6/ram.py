from Vehicle import Vehicle
from gaspowered import GasPowered

class Dodge_Ram(Vehicle, GasPowered):
    def __init__(self, model, manufacturer, horsepower, wheel_count, capacity):
        Vehicle.__init__(self, "Ram", "Dodge", 395, 4)
        GasPowered.__init__(self, 26)


        def drive(self):
            GasPowered.drive(self, 6)