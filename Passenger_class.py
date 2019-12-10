from Human_class import *

class Passenger(Human):
    def __init__(self, name, passportnumber):
        super().__init__(self, name)
        self.passportnumber = passportnumber
