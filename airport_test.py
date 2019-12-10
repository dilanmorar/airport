from airport_run import *

def test_create_passenger():
    passenger = Passenger('Joana Thomson', 'B343123')
    assert passenger.name == 'Joana Thomson'
    assert passenger.passportnumber == 'B343123'

def test_passenger_limited_info():
    pass

def test_create_plane():
    plane = Plane('1024')
    assert plane.planenumber == '1024'

def test_create_flight():
    flight = Flight('1024', 'US', 'UK', [])
    assert flight.planenumber == '1024'
    assert flight.destination == 'US'
    assert flight.origin == 'UK'
    assert flight.passengerlist == []

def test_flight_limited_info():
    test_flight = Flight()
    assert test_flight.planenumber == 'None'
    assert test_flight.destination == 'None'
    assert test_flight.origin == 'None'
    assert test_flight.passengerlist == ['None']

def test_add_plane():
    test_flight = Flight()
    test_flight.add_plane('1024')
    assert test_flight.plane == '1024'

def test_add_destination():
    test_flight = Flight('1024', 'None', 'UK', [])
    test_flight.add_passenger('US')
    assert test_flight.destination == 'US'

def test_add_origin():
    test_flight = Flight('1024', 'US', 'UK', [])
    test_flight.add_origin('UK')
    assert test_flight.origin == 'UK'

def test_add_passenger():
    test_flight = Flight('1024', 'US', 'UK', [])
    test_flight.add_passenger('Joana Thomson')
    assert test_flight.passengerlist[0] == 'Joana Thomson'


