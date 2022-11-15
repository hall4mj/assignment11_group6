'''
Name: John O'Connell, Matthew Hall
email: oconnejh@ucmail.uc.edu, hall4mj@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Making an API call with a URL
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
   
for farm in parsed_json['data']:
    print(farm["name"])
   
