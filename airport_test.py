from airport_run import *

def test_create_passenger(self):
    passenger = Passenger('Joana Thomson', 'B343123')
    assert passenger.name == 'Joana Thomson'
    assert passenger.passportnumber == 'B343123'

# def create_plane(self):
#     plane = Plane()
#     assert plane.planenumber
#
# def create_flight(self):
#     flight = Flight()
#     assert flight.plane
#     assert flight.destination
#     assert flight.origin
#     assert flight.passengerlist