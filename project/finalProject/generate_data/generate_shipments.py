'''
Purpose:
    generate all registered shipment in "Enviolo!" startup.

Methods:
    - generate_shipment: generate a shipment data.
Utility methods
    - assign_entity: assign values of other DB into agents using
        specified fields.
    - generate_tracking: generate tracking value into shipments.
    - generate_product: generate a list of name of products to send.
'''
from datetime import timedelta, datetime
from random import randint, shuffle
from os import path, getcwd
from math import floor


def generate_tracking():
    '''
    Generate a tracking code for shipments
    return a string of tracking code
    '''
    alphabet = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'I', 'K','L','M',
                'N', 'O', 'P', 'Q', 'R', 'L', 'T','W', 'X', 'Y','Z']
    first_letter_tracking = randint(0, len(alphabet)-1)
    second_letter_tracking = randint(0, len(alphabet)-1)
    thrid_letter_tracking = randint(0, len(alphabet)-1)
    number_tracking = str(randint(1, 9999999)).zfill(7)

    return '{}{}{}{}'.format(alphabet[first_letter_tracking],
                             alphabet[second_letter_tracking],
                             alphabet[thrid_letter_tracking],
                             number_tracking)


def assign_entity(agent_list, entities_percentage, default_value,
                  assign_field):
    '''
    associate agents into entities based in percentage of members per entities.
    Params:
     - agent_list (list) : list of shipment.
     - entities_percentage (tuple list): entities will associated in agents. pair type
          float-dict
     - default_value (dict) : value default if need to complete to avoid null cell
     - assign_field (str) : name of field will assign this value
    Return modified agents list
    '''
    shuffle(agent_list)
    agent_size = len(agent_list)
    indexAgent = 0

    for entity in entities_percentage:
        counting = 0
        while counting < floor(agent_size*entity[1]) and indexAgent < agent_size:
            agent_list[indexAgent][assign_field] = entity[0]
            indexAgent += 1
            counting += 1

    while indexAgent < agent_size:
        agent_list[indexAgent][assign_field] = default_value
        indexAgent += 1

    return agent_list


def generate_product():
    '''
    generate a product to send in shipment
    return a string of product
    '''
    path_base = path.abspath(getcwd())
    product_manager = []

    for line in open(path_base+"/data_generate/Producto.txt"):
        product_manager.append(line)

    return product_manager


def generate_shipment(start_date, end_date, number, start_id,
                   associated_city, default_city, associated_enterprise,
                   default_enteprise):
    '''
        generate a list of shipments .
    Params:
	 - start_date (datetime): minimum datetime to create shipment in system.
	      this is required
	 - end_data (datetime): maximum datetime to create shipment in system.
	      this is required.
	 - number (int): number of agent will generated. this is required.
	 - start_id (int) : number start of Sequential ID.
	 - associated_city (tuple list) : percentagae vehicle need use by agents.
	      this is required.
     Return:
      - agents (Array of dict): contain all shipment.
    '''
    shipment_list = []
    package_size = ['ss', 's', 'm', 'l', 'xl', 'xxl']
    type_service = ['B2B', 'B2C', 'B2B-reverse', 'B2C-reverse']
    product_list = generate_product()
    day_range = end_date - start_date

    for index_num in range(number):
        diff_range = timedelta(days=randint(0, day_range.days)) # mejorar tiempo
        shipment_list.append({
            'created': (start_date + diff_range).strftime("%m/%d/%YT%H:%M:%S"),
            'tracking': generate_tracking(),
            'id':  start_id+index_num,
            'product': {
                'name': product_list[randint(0, len(product_list)-1)],
                'quantity': randint(1, 50),
                'package_size': package_size[randint(0, len(package_size)-1)]
            },
            'type': type_service[randint(0, len(type_service)-1)]
        })

    shipment_list = assign_entity(shipment_list, associated_city,
                           default_city, 'city_id')
    shipment_list = assign_entity(shipment_list, associated_enterprise,
                           default_enteprise, 'enteprise_id')

    return shipment_list

'''
enterprise_client = [
    ("nestle", 0.25),
    ("VTEX", 0.30),
]
enterprise_default = "chazki"
city_list = [
    ('arequipa', 0.8),
    ('lima', 0.15),
]
city_default = "iquitos"
print(generate_shipment(datetime(2020, 1, 1, 0, 0, 0),
                  datetime(2021, 1, 1, 0, 0, 0), 1000,  0,
                  city_list, city_default, enterprise_client,
                  enterprise_default))
'''

