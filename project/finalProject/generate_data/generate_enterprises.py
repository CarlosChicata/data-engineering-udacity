'''
Purpose:
    generate all associated enterprises in "Enviolo!" startup.

Methods:
    - generate_enterprises: generate all enteprises in database.
Utility methods
    - generate_enterprises_manager: get name of enteprises.
    - generate_phone: generate a fake phone number of enteprise.
'''
from datetime import timedelta, datetime
from random import randint, shuffle
from os import path, getcwd


def generate_enterprises_manager():
    '''
    generate a list of enterprises with data to generate list
    return a list of entities
    '''
    path_base = path.abspath(getcwd())
    enterprises_manager = []

    for line in open(path_base+"/data_generate/Empresas.txt"):
        enterprises_manager.append({
            'name': line
        })

    return enterprises_manager


def generate_phone():
    '''
    generate a phone number
    return a string as phone number
    '''
    first_number = str(randint(1000, 9999))
    second_number = str(randint(1, 999)).zfill(3)

    return '99{}{}'.format(first_number, second_number)


def generate_enterprises(start_date, end_date, number, city_list):
    '''
    Generate enterprises to send shipments
    Params:
     - start_date (datetime): minimum datetime to register agent in system.
          this is required
     - end_data (datetime): maximum datetime to register agent in system.
          this is required.
     - number (int): number of agent will generated. this is required.
     - city_list (list): list of city is workign now. this is required.
    Return modified agents list
    '''
    enterprises_manager = generate_enterprises_manager()

    if len(enterprises_manager) < number:
        print("Error: max capacity of generated enterprises passed")
        return None

    enterprises_list = []
    shuffle(enterprises_manager)
    day_range = end_date - start_date

    for index in range(number):
        diff_range = timedelta(days=randint(0, day_range.days))

        enterprises_list.append({
            'name': enterprises_manager[index],
            'id': index+1,
            'deleted': False,
            'phone': generate_phone(),
            'created': (start_date + diff_range).strftime("%m/%d/%YT%H:%M:%S"),
            'city': city_list[randint(0, len(city_list)-1)],
        })

    return enterprises_list


'''
test 
print(generate_enterprises(
    datetime(2019, 4, 4, 4, 4, 4),
    datetime(2020, 4, 4, 4, 4, 4),
    20,
    [1, 0, 3, 4, 5, 6]))
'''
