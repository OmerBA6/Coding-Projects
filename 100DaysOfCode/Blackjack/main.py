from art import logo
import os
import random 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_final_hands(user_final_hand, computer_final_hand):
    print (f"   Your final hand: {user_final_hand[:]}, final score: {str(sum(user_final_hand))}")
    print (f"   Computer's final hand: {computer_final_hand[:]}, final score: {str(sum(computer_final_hand))}")
          
def print_user_state(user_current_cards):
    print (f"   Your cards: {user_current_cards[:]}, current score: {str(sum(user_current_cards))}")

def is_over_the_limit(user_current_cards):
    return sum(user_current_cards) > 21

def check_win(user1_hand, user2_hand):
    return (sum(user1_hand) > sum(user2_hand))

def check_draw(user1_hand, user2_hand):
    return (sum(user1_hand) == sum(user2_hand))

def replace_ace_value(hand_of_cards):
    while 11 in hand_of_cards:
        hand_of_cards.remove(11)
        hand_of_cards.append(1)
    return hand_of_cards



def blackjack():
    os.system('clear')
    print(logo)

    user_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    computer_cards = [cards[random.randint(0, 12)]]
    print_user_state(user_cards)
    print (f"   computer's first card: {computer_cards[0]}")

    hit_another_card = input("Type 'y' to get another card, type 'n' to pass: ") == 'y'
    while (hit_another_card) and not(is_over_the_limit(user_cards)):
        user_cards.append(cards[random.randint(0, 12)])
        if(is_over_the_limit(user_cards) and 11 in user_cards):
            user_cards = replace_ace_value(user_cards)
        
        print_user_state(user_cards)
        print (f"   computer's first card: {computer_cards[0]}")

        if not is_over_the_limit(user_cards):
            hit_another_card = (input("Type 'y' to get another card, type 'n' to pass: ") == 'y')

    #Draw cards for the computer
    while (sum(computer_cards) < 17):
        computer_cards.append(cards[random.randint(0, 12)])
        if(sum(computer_cards) > 17 and 11 in computer_cards):
            computer_cards = replace_ace_value(computer_cards)



    if(is_over_the_limit(user_cards)): #User over the limit
        print_final_hands(user_cards, computer_cards)
        print("You went over. You lose 😭")
    elif(is_over_the_limit(computer_cards)): #Computer over the limit
        print_final_hands(user_cards, computer_cards)
        print("Opponent went over. You win 😁")
    elif(check_win(user_cards, computer_cards)): #User win
        print_final_hands(user_cards, computer_cards)
        print("You win 😁")
    elif(check_win(computer_cards, user_cards)): #Computer win
        print_final_hands(user_cards, computer_cards)
        print("You Lose 😭")
    elif(check_draw(user_cards, computer_cards)): #It is a Draw
        print_final_hands(user_cards, computer_cards)
        print("Draw 🙃")

    if (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y'):
        blackjack()



want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if want_to_play == 'y':
    blackjack()
