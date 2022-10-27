import random
import keys
# Lab - Built-in Data Structures II
# Task 1: A List of Destination Dictionaries
destination_houston = {
    'destination' : 'Houston',
    'restaurant' : ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse', 'Taste of Texas Restaurant'],
    'transportation' : ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber', 'Train'],
    'entertainment' : ['Amusement Park', 'Hiking', 'Circus', 'Arcade', 'Art Exhibit'],
    }
destination_dallas = {
    'destination' : 'Dallas',
    'restaurant' : ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse', 'Taste of Texas Restaurant'],
    'transportation' : ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber', 'Train'],
    'entertainment' : ['Amusement Park', 'Hiking', 'Circus', 'Arcade', 'Art Exhibit'],
    }
destination_austin = {
    'destination' : 'Austin',
    'restaurant' : ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse', 'Taste of Texas Restaurant'],
    'transportation' : ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber', 'Train'],
    'entertainment' : ['Amusement Park', 'Hiking', 'Circus', 'Arcade', 'Art Exhibit'],
    }
destination_sanantonio = {
    'destination' : 'San Antonio',
    'restaurant' : ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse', 'Taste of Texas Restaurant'],
    'transportation' : ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber', 'Train'],
    'entertainment' : ['Amusement Park', 'Hiking', 'Circus', 'Arcade', 'Art Exhibit'],
    }

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 2: Refactor The Random Generator
def generate_random_item(list): #generate a random item from a list
    random_item = random.choice(list)
    return random_item

def generate_random_item_from_dictionary1(dictionary): #refactored code
    if dictionary == str(dictionary):
        return dictionary
    else:
        return random.choice(dictionary)
    
# print(generate_random_item_from_dictionary1(destination_austin['destination'])) #test

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Task 3: New Data
destination_houston['climate'] = 'humid subtropical'
destination_dallas['climate'] = 'humid subtropical'
destination_austin['climate'] = 'humid subtropical'
destination_sanantonio['climate'] = 'transitional humid subtropical'
#first method
# austin_destination = generate_random_item_from_dictionary(destination_austin['destination'])
# austin_climate = generate_random_item_from_dictionary(destination_austin['climate'])
# print(f'In {austin_destination}, the climate is {austin_climate}!')
#different method
def generate_random_item_from_dictionary2(dictionary): #refactored code
    destination_property = ''
    restaurant_property = ''
    transportation_property = ''
    entertainment_property = ''
    climate_property = ''
    for field, property in dictionary.items():
        if field == 'destination':
            destination_property = property
        elif field == 'restaurant':
            restaurant_property = random.choice(property)
        elif field == 'transportation':
            transportation_property = random.choice(property)
        elif field == 'entertainment':
            entertainment_property = random.choice(property)
        elif field == 'climate':
            climate_property = property
    # return destination_property, restaurant_property, transportation_property, entertainment_property, climate_property
    print(f'In {destination_property} the climate is generally a {climate_property} area.')
# generate_random_item_from_dictionary2(destination_dallas)

# destination_dallas_tuple = generate_random_item_from_dictionary2(destination_dallas) #Can return a tuple to a variable such as this one for more precise prints. This creates a tuple with random data.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Task 4: Accessing Dictionary Values with Variables
