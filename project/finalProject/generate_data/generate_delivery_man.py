'''
Purpose:
    generate all delivery man in "Enviolo!" startup.

Methods:
    - generate_agent: generate all agent (delivery man) for dataset.

Utility methods
    - user_name_list: create manager to assign first name and
        last name of agents.
    - assign_entity: assign values of other DB into agents using
        specified fields.
'''
from datetime import timedelta, datetime
from random import randint, shuffle
from os import path, getcwd
from math import floor


def user_name_list():
    '''
    Generate a manage to name and lastname of user
    return a two dictionary with name and lastname. those are number-string pair
    '''
    path_base = path.abspath(getcwd())
    lastname_manager = {}
    firstname_manager = {}
    counting = 0

    for line in open(path_base+"/data_generate/Apellido.txt"):
        lastname_manager.update({ counting: line })
        counting += 1

    counting = 0

    for line in open(path_base+"/data_generate/Nombres.txt"):
       firstname_manager.update({ counting: line })
       counting += 1

    return firstname_manager, lastname_manager


def assign_entity(agent_list, entities_percentage, default_value,
                  assign_field):
    '''
    associate agents into entities based in percentage of members per entities.
    Params:
     - agent_list (list) : list of agents.
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


def generate_agent(start_date, end_date, number, start_id,
                   associated_vehicle, associated_city,
                   default_vehicle, default_city):
    '''
    generate a list of agents to  delivery shipments.
    Params:
	 - start_date (datetime): minimum datetime to register agent in system.
	      this is required
	 - end_data (datetime): maximum datetime to register agent in system.
	      this is required.
	 - number (int): number of agent will generated. this is required.
	 - start_id (int) : number start of Sequential ID.
	 - associated_enterprise (tuple list): percentage need agents to associated
	      a specified enterprise. This is required.
	 - associated_vehicle (tuple list): percentage vehicle need use by agents.
	      this is required.
	 - associated_city (tuple list) : percentagae vehicle need use by agents.
	      this is required.
     - default_enterprise (tuple): default value for associated_enterprise. this
         is required.
     - default_vehicle (tuple): default value for associated_vehicle. this is
         required.
     - default_city (tuple): default value for associated_city. this is
         required.
     Return:
      - agents (Array of dict): contain all agents.
    '''
    agent_list = []
    day_range = end_date - start_date
    firstname_list, lastname_list = user_name_list()
    firstname_len, lastname_len = len(firstname_list), len(lastname_list)

    for index_num in range(number):
        diff_range = timedelta(days=randint(0, day_range.days))
        firstname = firstname_list[randint(0, firstname_len-1)]
        lastname = lastname_list[randint(0, lastname_len-1)]
        lastname_2 = lastname_list[randint(0, lastname_len-1)]

        agent_list.append({
           'id': start_id + index_num,
           'created': (start_date + diff_range).strftime("%m/%d/%YT%H:%M:%S"),
           'firstname': firstname[:-1],
           'lastname': lastname[:-1] + " " + lastname_2[:-1],
           'username': firstname[0] + lastname[:-1] + str(index_num),
           'is_active': True if randint(0, 100) > 50 else False,
           'remove': False,
        })

    agent_list = assign_entity(agent_list, associated_vehicle,
                           default_vehicle, 'vehicle')
    agent_list = assign_entity(agent_list, associated_city, default_city,
                               'city')

    return agent_list

