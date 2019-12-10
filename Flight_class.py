from Passenger_class import *
from Plane_class import *

class Flight():
    def __init__(self, planenumber = 'None', destination = 'None', origin = 'None', passengerlist = ['None']):
        self.planenumber = planenumber
        self.destination = destination
        self.origin = origin
        self.passengerlist = passengerlist

    def add_passenger(self, passenger):
        passenger_name = self
        passenger_name.passengerlist.append(passenger)

    def add_plane(self, plane):
        self.plane = plane

    def add_destination(self, destination):
        self.destination = destination

    def add_origin(self, origin):
        self.origin = origin

passengerlist = []
