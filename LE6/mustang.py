from Vehicle import Vehicle
from gaspowered import GasPowered

class Ford_Mustang(Vehicle, GasPowered):
    def __init__(self, model, manufacturer, horsepower, wheel_count):
        Vehicle.__init__(self, "Mustang", "Ford", 460, 4)
        GasPowered.__init__(self, 20)

    def drive(self):
        GasPowered.drive(self, 4)