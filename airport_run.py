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
    flight = Flight(plane, destination, origin)
    return flight.plane
    return flight.destination
    return flight.origin