'''
Created on Nov 14, 2022

@author: Matthew Hall
'''
# main.py
import json # Built-in, no pip install required
import requests # Add with pip

response = requests.get('https://api.ers.usda.gov/data/arms/state?api_key=9hHR7zpf05bUT4YMMRWTgRujw3aIC4WAvlFB7Vzb')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    
#print(parsed_json)
#print(parsed_json['data'][0]['description'])
#print(parsed_json['data'][0]['directionsInfo'])
    
status = parsed_json['status']        # The number of parks that were returned
print(status)    


for farm in parsed_json['data']: # Get the value associated with parsed_json['data']   
    print (farm)
