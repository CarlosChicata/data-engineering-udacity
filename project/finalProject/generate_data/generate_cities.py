'''
Purpose:
    generate all availables cities in "Enviolo!" startup.

Methods:
    - generate_cities: generate all cities into DB
Utility methods
    - generate_cities_manager: assign values for  cities in
        specified fields.
'''
from datetime import timedelta, datetime
from random import randint, shuffle
from os import path, getcwd


def generate_cities_manager():
    '''
    generate a list of cities with data to generate list
    return a list of entities
    '''
    path_base = path.abspath(getcwd())
    cities_manager = []

    for line in open(path_base+"/data_generate/Ciudades.txt"):
        line = line.split(";")
        cities_manager.append({
            'name': line[0],
            'language': line[3],
            'country': line[1],
            'currency': line[2],
        })

    return cities_manager


def generate_cities(start_date, end_date, number):
    '''
    Generate cities to work
    Params:
	 - start_date (datetime): minimum datetime to register agent in system.
	      this is required
	 - end_data (datetime): maximum datetime to register agent in system.
	      this is required.
	 - number (int): number of agent will generated. this is required.
    Return modified agents list
    '''
    cities_manager = generate_cities_manager()

    if len(cities_manager) < number:
        print("Error: max capacity of generated city passed")
        return None

    cities_list = []
    shuffle(cities_manager)
    day_range = end_date - start_date

    for index in range(number):
        diff_range = timedelta(days=randint(0, day_range.days))

        cities_list.append({
            'name': cities_manager[index]["name"],
            'language': cities_manager[index]["language"],
            'country': cities_manager[index]["country"],
            'currency': cities_manager[index]["currency"],
            'id': index+1,
            'created': (start_date + diff_range).strftime("%m/%d/%YT%H:%M:%S"),
        })

    return cities_list

'''
testing

print(generate_cities(datetime(2019, 4, 4, 4, 4, 4), datetime(2020, 4, 4, 4, 4, 4), 10))
'''
