'''
Purpose:
    generate all vehicles used for delivery man in "Enviolo!" startup.

Methods:

Utility methods

'''
from datetime import timedelta, datetime
from random import randint


def plate_vehicle(type):
    alphabet = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'I', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'L', 'T', 'W', 'X', 'Y', 'Z']

    if type in ['Van', "Automovil"]:
        first_letter = randint(0, len(alphabet)-1)
        second_letter = randint(0, len(alphabet)-1)
        number_plate = str(randint(1, 999999)).zfill(6)
        return "{}{}{}".format(
            alphabet[first_letter],
            alphabet[second_letter],
            number_plate
        )
    elif type in ["Motocarro", "Motocicleta"]:
        first_letter = randint(0, len(alphabet)-1)
        second_letter = randint(0, len(alphabet)-1)
        thrid_letter = randint(0, len(alphabet)-1)
        number_plate = str(randint(1, 99999)).zfill(5)
        return "{}{}{}".format(
            alphabet[first_letter],
            alphabet[second_letter],
            alphabet[thrid_letter],
            number_plate
        )
    else:
        return ''


def generate_vehicle(start_date, end_date, number):
    '''
    generate vehicle will use for delivery man.
    Params:
	 - start_date (datetime): minimum datetime to register expiration date
	    of document in system. this is required
	 - end_data (datetime): maximum datetime to register expiration date
	    of document in system. this is required.
	 - number (int): number of agent will generated. this is required.
    return a list of vehicle
    '''
    type_list = ["Van", "Motocicleta", "Bicicleta", "Automovil",
        "Ciclomotor", "Motocarro"]
    vehicle_list = []
    day_range = end_date - start_date

    for index in range(number):
        diff_range = timedelta(days=randint(0, day_range.days))
        diff_range2 = timedelta(days=randint(0, day_range.days))
        type_vehicle = type_list[randint(0, len(type_list)-1)]

        vehicle_item = {
            'type': type_vehicle,
            'plate': plate_vehicle(type_vehicle),
            'id': index
        }
        if type_vehicle not in ["Bicicleta", 'Ciclomotor']:
            vehicle_item['expirate_licence_date'] = (start_date + diff_range).strftime("%m/%d/%YT%H:%M:%S")
            vehicle_item['expiration_soat_date'] = (start_date + diff_range2).strftime("%m/%d/%YT%H:%M:%S")

        vehicle_list.append(vehicle_item)

    return vehicle_list


print(generate_vehicle(datetime(2020, 1, 1, 0, 0, 0),
                  datetime(2021, 1, 1, 0, 0, 0), 1000))
