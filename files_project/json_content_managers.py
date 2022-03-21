import json

with open('friends_json.txt', 'r') as file: # this is the file pointer
    file_contents = json.load(file)      # the json.load - reads the entire file AND turns it into a dictionary

print(file_contents['friends'][0])

# To write a dictionary as a JSON file...

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, car_file)


# Example of Json string -> Dictionary
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])

# fp = file pointer
# Serialize = means turn into a string
# .dumps() turns what ever construct you have into a json string
# json  allows you to use Lists and Dictionaries NOT tuples. Try to avoid objects in a json bc they load as a string
# if you want to turn objects into json, make sure to describe objects using a dictionary out of the objects properties and their values

