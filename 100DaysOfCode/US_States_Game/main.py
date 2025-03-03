import pandas as pd
import turtle
from stateTurtle import StateTurtle

IMAGE_PATH = 'blank_states_img.gif'
CSV_FILE_PATH = '50_states.csv'


screen = turtle.Screen()
screen.title("U.S States game")
screen.setup(height=500)
image = IMAGE_PATH
screen.addshape(image)
turtle.shape(image)


states_data = pd.read_csv(CSV_FILE_PATH)


# Make a list of all the states names
list_of_states_names = states_data.state.to_list()

guessed_states = []
user_guess = ''
# Game loop
while len(guessed_states) < 50 and not user_guess == 'Exit':
    user_guess = screen.textinput(title=f"Guess A State | {len(guessed_states)}/50", prompt="Enter a state's name: ").title()

    if user_guess == 'Exit':
        break
    if user_guess in list_of_states_names:
        correct_state = states_data[states_data['state'] == user_guess]
        correct_state_location_tuple = (correct_state.x.item(), correct_state.y.item())
        correct_state_turtle = StateTurtle(user_guess, correct_state_location_tuple)
        guessed_states.append(user_guess)


states_not_guessed = [state for state in list_of_states_names if state not in guessed_states]
states_not_guessed_data = pd.DataFrame(states_not_guessed)
states_not_guessed_data.to_csv("States To Learn.csv")
