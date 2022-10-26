import random
import string
# #for task 2 favorite_number = 7
# #Task 2: Generate a random number
# def find_difference(): #Function to find difference between favorite number and randomly generated number between range(0,10)
#     random_number = random.randrange(10)
#     difference = random_number - favorite_number
#     if random_number < 7:
#         difference *= -1
#     print(f'The random number is {random_number}!')
#     print(f'The difference between your favorite number {favorite_number}, and the random number{random_number}, is {difference}!' )
#     #can return difference if wanted to using (return difference) 
# find_difference()

# #Task 3: Repeat cod with loop
# def find_favorite_number():
#     user_favorite_number = input('What is your favorite number between 0 and 10?') #Can have a function created for this variable, but for the sake of the task, we're assuming the user will input an integer
#     guess_counter = 0
#     random_number = 0
#     correct_guess = False
#     while correct_guess == False:
#         random_number = random.randrange(11)
#         if random_number == int(user_favorite_number):
#             correct_guess = True
#             print(f'It took the computer {guess_counter} times to guess your favorite number {user_favorite_number}!')
#         elif random_number != user_favorite_number:
#             guess_counter += 1
#             correct_guess = False

# find_favorite_number()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Lab - Problem Solving II

#Task 1: Reverse a string
# 1. define a funtion to call whenever a string is needed to be reversed
# 2. create a variable to hold a string with nothing
# 3. make a for loop for each element in a backwards index of the word. (start, end, step)
# 4. add each letter to the 'variable that holds nothing' by using +=
# 5. print the end variable after the for loop has been completed autmatically
# 6. call the funtion with its parameter
# def reverse_string(word): 
#     reversed_word = ''
#     for element in range(len(word) -1, -1, -1):
#         reversed_word += word[element]
#     print(f' Here is your word reversed: {reversed_word}')

# reverse_string(input('What word would you like to be reversed?'))

#Task 2: Capitalize a Letter
# 1. research how to capitalize the first letter in each word of a string (string.capwords())
# 2. import string module to use capwords variable
# 2. define a funtion to capitalize the letter of each word
# 3. set a variable 'final_result' equal to ''
# 4. create a while loop

# def capitalize_each_word(words):
#     return string.capwords(words)

# final_result = capitalize_each_word(input('What string of words would you like to be capitalized?'))
# print(final_result)

# Same task but more complicated to find a better understanding
# 1. define a function to capitalize the first letters of a string (capitalize_first_letters())
# 2. set a user input variable so the user can input any words they want
# 3. set a variable for a new_string to capture the end result
# 4. create a for loop to find each element in list (list is the users input split into multiple strings)
# 5. add each element of the list to the new_string variable and capitalize the first letters
# 6. return the new_string back to where it's called
# 7. create a variable outside the function (final_string) and set it to the function
# 8. print that variable to test out if works #can print out function as it is without setting it equal to a variable

# def capitalize_first_letters():
#     user_input = input('Which words would you like to capitalize?')
#     new_string = ''
#     for element in user_input.split():
#         new_string += element.capitalize() + ' '
#     return new_string

# final_string = capitalize_first_letters()
# print(final_string)

# Task 3: Palindrome
# 1. get reverse_string function from task 1 to use
# 2. revise function to return a reversed word
# 3. define a function to find palindromes (find_palindrome())
# 4. set a variable (user_input) to ask for the users input
# 5. set a variable (new_user_input) to lowercase string user inputted 
# 6. set a variable (word_reversed) equal to a function that reverses new_user_input
# 7. set True or False variable to capture the result
# 8. create an if statement and ask if new_user_input is equal to word_reversed. If so print out that the users_input is a palindrome. Set the True/False variable to True
# 9. create an else statement and make it opposite of #8
# 10. return the True or False variable

# def reverse_string(word): 
#     reversed_word = ''
#     for element in range(len(word) -1, -1, -1):
#         reversed_word += word[element]
#     return reversed_word

# def find_palindrome():
#     user_input = input('What word, phrase, or sequence do you want to know is or is not a palindrome?')
#     new_user_input = user_input.lower()
#     word_reversed = reverse_string(new_user_input)
#     palindrome = True
#     if new_user_input == word_reversed:
#         palindrome = True
#         print(f'{user_input} is a palindrome!')
#         return palindrome
#     else:
#         palindrome = False
#         print(f'{user_input} is not a palindrome!')
#         return palindrome
    
# find_palindrome()

# Task 4: Compress a String of Characters
# 1. define a function to compress a string (get_compressed_string)
# 2. set a variable (string) to capture a users input
# 3. set a variable (compress_string) to catpure final string
# 4. set a variable to count strings (counter)
# 5. create a for loop to find each element in a rangle of the length of the string
# 6. create an if statement to add to the counter each time the element is the same
# 7. create an else statement to add to the compressed_string variable each time the element changes. Also, reset the counter
# 8. add the last element plus its counter
# 9. print the final string (compressed_string)

def get_compressed_string():
    string = input('What characters would you like to compress?')
    compressed_string = ''
    counter = 1
    for char in range(len(string)-1):
        if string[char] == string[char+1]:
            counter += 1
        else:
            compressed_string += string[char] + str(counter)
            counter = 1
    compressed_string += string[char+1] + str(counter)
    print(compressed_string)

get_compressed_string()