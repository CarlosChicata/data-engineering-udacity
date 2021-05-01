import os
from datetime import timedelta
from random import randint
from os import path, getcwd


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


def assign_entity(agent_list, entities_percentage, default_value):
   '''
   associate agents into entities based in percentage of members per entities.
   Params:
    - agent_list (list) : list of agents.
    - entities_percentage (tuple list): entities will associated in agents. pair type
         float-dict
    - default_value (dict) : value default if need to complete to avoid null cell
   Return modified agents list
   '''




def generate_agent(start_date, end_date, number, start_id,
                   associated_enterprise, associated_vehicle, associated_city):
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
   Return:
	- agents (Array of dict): contain all agents.
   '''
   agent_list = []
   day_range = end_date - start_date
   firstname_list, lastname_list = user_name_list()
   firstname_len, lastname_len = len(firstname_list), len(lastname_list)

   for index_num in range(number):
      diff_range = timedelta(minutes=randint(0, day_range))
      firstname = firstname_list[randint(0 , firstname_len)]
      lastname = lastname_list[randint(0, lastname_len)]

      agent_list.append({
         'id': start_id + index_num,
         'created': start_date + diff_range,
         'firstname': firstname,
         'lastname': lastname,
         'username': firstname[0] + lastname + str(index_num),
         'is_active': True if randint(0, 100) > 50 else False,
         'remove': False,
      })

