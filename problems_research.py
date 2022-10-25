import random
# for task 2 favorite_number = 7
#Task 2: Generate a random number
def find_difference(): #Function to find difference between favorite number and randomly generated number between range(0,10)
    random_number = random.randrange(10)
    difference = random_number - favorite_number
    if random_number < 7:
        difference *= -1
    print(f'The random number is {random_number}!')
    print(f'The difference between your favorite number {favorite_number}, and the random number{random_number}, is {difference}!' )
    #can return difference if wanted to using (return difference) 
find_difference()

#Task 3: Repeat cod with loop
def find_favorite_number():
    user_favorite_number = input('What is your favorite number 0 and 10?') #Can have a function created for this variable, but for the sake of the task, we're assuming the user will input an integer
    guess_counter = 0
    random_number = 0
    correct_guess = False
    while correct_guess == False:
        random_number = random.randrange(11)
        if random_number == int(user_favorite_number):
            correct_guess = True
            print(f'It took the computer {guess_counter} times to guess your favorite number {user_favorite_number}!')
        elif random_number != user_favorite_number:
            guess_counter += 1
            correct_guess = False

find_favorite_number()