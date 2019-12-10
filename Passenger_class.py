from Human_class import *

class Passenger(Human):
    def __init__(self, name, passportnumber):
        super().__init__(name)
        self.passportnumber = passportnumber
