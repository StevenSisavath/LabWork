import random
# Lab - Built-in Data Structures II
# Task 1: A List of Destination Dictionaries
destination_list = ['Houston', 'Dallas', 'Austin', 'San Antonio']
restaurant_list = ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse', 'Taste of Texas Restaurant']
transportation_list = ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber', 'Train']
entertainment_list = ['Amusement Park', 'Hiking', 'Circus', 'Arcade']
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
# Task 2: Refactor The Random Generator
def generate_random_item(list): #generate a random item from a list
    random_item = random.choice(list)
    return random_item

def generate_random_item_from_dictionary(dictionary): #refactored code
    if dictionary == str(dictionary):
        return dictionary
    else:
        return random.choice(dictionary)
    
print(generate_random_item_from_dictionary(destination_austin['destination']))