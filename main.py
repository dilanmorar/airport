from airport_run import *

while True:
    print('Choose option: ')
    print('1. create a passenger')
    print('2. choose a plane')
    print('3. choose a flight')
    user_choice = input('Choose one of the options above: ')

    if user_choice == '1':
        user_passenger_name = input('Name of passenger: ')
        user_passenger_passport_number = input('Passport number of passenger: ')
        create_passenger(user_passenger_name, user_passenger_passport_number)
        break

    elif user_choice == '2':
        user_plane_choice = input('Name of plane: ')
        create_plane(user_plane_choice)
        break

    elif user_choice == '3':
        user_plane = input('Name of plane: ')
        user_destination = input('Destination: ')
        user_origin = input('Origin: ')
        create_flight(user_plane, user_destination, user_origin, passengerlist)
        break

    elif user_choice == '4':

        break

    elif user_choice == '5':

        break

    elif user_choice == '6':

        break

    else:
        break