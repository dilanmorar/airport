from airport_run import *

flight1 = Flight('Flight 1', 'New York', 'London')
flight2 = Flight('Flight 2', 'Barcelona', 'Glasgow')
flight3 = Flight('Flight 3', 'Amsterdam', 'Budapest')
flights = []
flights.extend([flight1, flight2, flight3])
passengerlist = []

while True:
    print('Choose option: ')
    print('1. create a passenger')
    print('2. choose a flight')
    print('3. add passenger to flight')
    user_choice = input('Choose one of the options above: ')

    if user_choice == '1':
        user_passenger_name = input('Name of passenger: ')
        user_passenger_passport_number = input('Passport number of passenger: ')
        create_passenger(user_passenger_name, user_passenger_passport_number)
        break

    elif user_choice == '2':
        number_of_flights = len(flights)
        count = 0
        print('List of flights: ')
        while count<=number_of_flights:
            print(flights[count].planenumber + ':' + ' from ' + flights[count].origin + ' to ' + flights[count].destination)
            count+=1
        else:
            break

    elif user_choice == '3':
        chosen_passenger = input('What passenger: ')
        chosen_flight = input('What flight: ')
        if chosen_flight == 'Flight 1':
            flight1.add_passenger(chosen_passenger)
        elif chosen_flight == 'Flight 2':
            flight2.add_passenger(chosen_passenger)
        elif chosen_flight == 'Flight 3':
            flight3.add_passenger(chosen_passenger)
        else:
            print('Flight does not exist')
            break
        break
    else:
        break