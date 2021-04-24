def generate_agent(start_date, end_date, number, associated_enterprise, associated_vehicle):
   '''
   generate a list of agents to  delivery shipments.

   Params:
	- start_date (datetime): minimum datetime to register agent in system. 
	    this is required
	- end_data (datetime): maximum datetime to register agent in system. this is 
            required.
	- number (int): number of agent will generated. this is required.
	- associated_enterprise (dict): percentage need agents to associated a specified 
	    enterprise. This is required.
	- associated_vehicle (dict): percentage vehicle need use by agents. this is required.
   Return
	- agents (Array of dict): contain all agents.
   '''
