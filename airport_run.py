from Passenger_class import *
from Plane_class import *
from Flight_class import *

def create_passenger(name, passportnumber):
    passenger = Passenger(name, passportnumber)
    return passenger.name
    return passenger.passportnumber

def create_plane(planenumber):
    plane = Plane(planenumber)
    return plane.planenumber

def create_flight(plane, destination, origin, passengerlist):
    flight = Flight(plane, destination, origin, passengerlist)
    return flight.plane
    return flight.destination
    return flight.origin
    return flight.passengerlist

def flight_limited_info():
    Flight()

def add_plane(self, plane):
    self.plane = plane

def add_destination(self, destination):
    self.destination = destination

def add_origin(self, origin):
    self.origin = origin

def add_passenger(self, added_passenger):
    self.passengerlist.append(added_passenger)