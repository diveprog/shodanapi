#!/usr/bin/env python

import shodan
import sys
import requests
from shodan.helpers import iterate_files, open_file, write_banner
import json 
from datetime import datetime

# Configuration
API_KEY = "UF9dtet3HwQzTkntSCAuJz1KRtYo0pBL"
s = datetime.now()


# Input validation
if len(sys.argv) == 1:
        print('Usage: %s <masukan domain>' % sys.argv[0])
        sys.exit(1)
print("Starting scan at :",s)
print("*"*50)
print('')

try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Perform the search
        query = ' '.join(sys.argv[1:])
        result = api.search(query)

        # Loop through the matches and print each IP
        for service in result['matches']:
                print(service['ip_str'], end = '')
                print("-", end = '')
                print(service['hostnames'])
            

except Exception as e:
        print('Error: %s' % e)
        sys.exit(1)
        
#hasil json
with open("data_shodanapi.json", "w") as write_file:
    json.dump(service, write_file)
       
        

