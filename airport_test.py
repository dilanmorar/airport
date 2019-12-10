from airport_run import *

def test_create_passenger(self):
    passenger = Passenger('Joana Thomson', 'B343123')
    assert passenger.name == 'Joana Thomson'
    assert passenger.passportnumber == 'B343123'

def test_create_plane(self):
    plane = Plane('1024')
    assert plane.planenumber == '1024'

def test_create_flight(self):
    flight = Flight('1024', 'US', 'UK')
    assert flight.plane == '1024'
    assert flight.destination == 'US'
    assert flight.origin == 'UK'
    assert flight.passengerlist