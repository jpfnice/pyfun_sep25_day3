"""
Write a Python scripts that implements the “Guess the Number” game.
The script will generate of a random integral number (use the module random) from 1 to 100, and ask you to guess it.
The script will tell you if each guess is too high or too low.
You win if you can guess the number within six tries.
"""

import random
# To generate an int in the range [1,100]:
secret=random.randint(1,100)

print(secret)

# This variable is used to count the number of attempts
# to guess the number done so far:
attempts=1 
MAX_NB_OF_ATTEMPTS=6

while attempts <= MAX_NB_OF_ATTEMPTS: # The maximum number of attempts is 6!
    while True:
        try:
            # The following formatted string print the current number of attempts:
                
            value=input(f"Enter an int between [1,100] ({attempts}/{MAX_NB_OF_ATTEMPTS}): ")
            value=int(value)
        except: # if an exception is raised (which ever it is):
            print (f"Your input ({value}) is not correct !")
            print("Please enter a new value.")
        else: # if no exception are raised:
            break
    
    if value < secret:
        print(value, "is too small!")
    elif value > secret:
        print(value, "is too large!")
    else:
        print("Bingo !", value, "was the secret number!")
        break # The secret number is found, I can leave the loop
    
    attempts = attempts + 1 # to increment the number of attempts
    
# I may leave the loop because the number as been found or 
# because I've reached the maximum number of attempts.
# I need to test that:
    
if attempts > 6:
    print("The secret number was:", secret)
    
    