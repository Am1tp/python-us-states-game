import turtle as t
import pandas as pd
from state_turtle import StateTurtle

screen = t.Screen()
screen.title("U.S States Game")
states_img = "blank_states_img.gif"
screen.addshape(states_img)
t.shape(states_img)

states_data = pd.read_csv("50_states.csv")
states_list = states_data.state.to_list()
correct_guesses = 0
previous_guesses = []

while correct_guesses < 50:

    if correct_guesses == 0:    # change text input title once correct guess > 0
        answer_state = screen.textinput(title="Guess The State", prompt="Guess the name of a state").title()
        user_answer = answer_state
    else:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="Guess the name of a state").title()
        user_answer = answer_state

    if user_answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in previous_guesses:
                missing_states.append(state)
        saved_data = pd.DataFrame(missing_states)
        saved_data.to_csv("States missed")
        exit()

    if user_answer in states_list:  # check user answer against list of states
        if user_answer in previous_guesses: # check if user has previously guessed the state
            continue
        else:
            state = states_data[states_data.state == user_answer] # if present return details of state
            x_coor = state.x.item() # return the value of x without the index
            y_coor = state.y.item() # return the value of y without the index
            state_name = state.state.item() # return the value of state (string)
            st = StateTurtle(x_coor, y_coor, state_name) # create turtle and go to location
            correct_guesses += 1
            previous_guesses.append(user_answer)
    else:
        continue    # repeat if state not in list or previous guesses

screen.exitonclick()







