from Passenger_class import *
from Plane_class import *

class Flight():
    def __init__(self, plane, destination, origin):
        self.plane = plane
        self.destination = destination
        self.origin = origin
        self.passengerlist = []

    def add_passenger(self, passenger):
        passenger_name = self
        passenger_name.passengerlist.append(passenger)