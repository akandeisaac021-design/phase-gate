
import random

def generate_a_random_number():

    random_number =random.randint(0, 100)

    return random_number

def manage_the_guessing_loop(random_number):
    user_attempts =1
    
    guessed_number =int(input("guess a number-->"))

    while guessed_number != random_number:
        if user_attempts <5:
            if random_number >guessed_number:
                guessed_number =int(input("Try guessing a higher number-->"))

            else:
                guessed_number =int(input("Try guessing a lower number-->"))

        else:
            return "Attempts exhausted: you failed"
        user_attempts +=1

    return "Well done: you have sense"

def to_control_the_range_of_the_guess_range(guessed_number):
    while guessed_number <0 || guessed_number >100:
        guessed_number =
