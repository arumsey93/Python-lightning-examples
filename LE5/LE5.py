# Define a class called Boat
# Give it a method that allows the boat to move that prints the speed it's moving
# Define a Class called Kayak
# Make it a derived class of Boat
# Give it a method called paddle that uses its inherited move method
# Make a Kayak instance and 'paddle' it

class Boat:

    def __init__(self, type, propulsion):
        self.type = type
        self.propulsion = propulsion

    def move(self, speed):
        return f"This boat moves at {speed} knots."

class Kayak(Boat):

    def __init__(self, passengers=1):
        super().__init__("kayak", "paddle")
        self.passengers = passengers

    def paddle(self):
        print(f'I like to go out in my Kayak. {self.move(3)}')

seaghost110 = Kayak()
seaghost110.paddle()



