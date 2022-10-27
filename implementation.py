# Lab - Built-in Data Structures
# Task 1: Dictionary, Set, and Tuple
# 1.
# months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December') #tuple for months
# print(f'National Pi Day occurs in {months[2]}!') #print for National Pi Day
months_dictionary = {
    'first_month': 'January',
    'second_month': 'February',
    3.14: 'March',
    'fourth_month': 'April',
    'fifth_month': 'May',
    'sixth_month': 'June',
    'seventh_month': 'July',
    'eighth_month': 'August',
    'ninth_month': 'September',
    'tenth_month': 'October',
    'eleventh_month': 'November',
    'twelvth_month': 'December',
    }
Pi = 3.14
print(months_dictionary[Pi])

# 2.
fruits_and_vegetables = ('Orange', 'Pineapple', 'Avacodo', 'Green Peas', 'Broccoli')
for element in fruits_and_vegetables:
    print(element)

# 3.
def print_user_info(): #Can be split into 2 functions. First to obtain the user's information. Second, to print the information. For the sake of the question, I combined the 2.
    first_name = input("What's your first name?")
    last_name = input("What's your last name")
    email_address = input("What's your email address?")
    phone_number = input("What's your phone number?")
    user_information_dictionary = {
        'first_name': first_name,
        'last_name': last_name,
        'email_address': email_address,
        'phone_number': phone_number
        }
    print('')
    print(f'''
Here is your profile information:
First Name: {user_information_dictionary['first_name']}
Last Name: {user_information_dictionary['last_name']}
Email Address: {user_information_dictionary['email_address']}
Phone Number: {user_information_dictionary['phone_number']}
    ''')
    print('')

#Task 2: List of Dictionaries
dads_dictionary = {
    'first_name': 'Mike',
    'second_name': 'Sisavath',
    'relation_to_me': 'Father',
}
moms_dictionary = {
    'first_name': 'Sone',
    'second_name': 'Sisavath',
    'relation_to_me': 'Mother',
}
brothers_dictionary = {
    'first_name': 'Bryant',
    'second_name': 'Sisavath',
    'relation_to_me': 'Brother',
}
immediate_family = [dads_dictionary, moms_dictionary, brothers_dictionary]

def find_first_names_and_relation():
    for value in immediate_family:
        print(f'''
First Name: {value['first_name']}
Relation: {value['relation_to_me']}''')
    print('')
find_first_names_and_relation()

# extra information to help for another time
        # for key, value in element.items():
        #     print('')
        #     print(f'The key {key} has a value of {value}')
        #     print('')