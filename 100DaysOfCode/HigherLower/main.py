import os
import random
import art 
from game_data import data

SCORE = 0


def print_current_score():
    global SCORE
    print(f"You're right! Current score: {SCORE}.")


def print_comparison(a, b):
    print (f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print (art.vs)
    print (f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")


def print_lost_screen():
    global SCORE
    os.system('clear')
    print (art.logo)
    print(f"Sorry, that's wrong. Final score: {SCORE}")



def higher_lower(a_received = []):
    global SCORE
    
    os.system('clear')
    print (art.logo)
    if not(SCORE == 0):
        print_current_score()

    if (a_received == []):
        a_object = random.choice(data)
    else:
        a_object = a_received
    
    b_object = random.choice(data)
    while (a_object == b_object):
        b_object = random.choice(data)

    print_comparison(a_object, b_object)

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower

    if (user_guess == 'a'):
        if(a_object['follower_count'] > b_object['follower_count']):
            SCORE += 1
            higher_lower(a_object)
        else:
            print_lost_screen()
    elif (user_guess == 'b'):
        if(b_object['follower_count'] > a_object['follower_count']):
            SCORE += 1
            higher_lower(b_object)
        else:
            print_lost_screen()
    else:
        print_lost_screen()



higher_lower()


