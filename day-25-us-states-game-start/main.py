<<<<<<< HEAD
import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# funtion used to get the coordinates
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor())

# answer_state = screen.textinput(title="guess the state ", prompt="whats the another state name ")

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
guess_states = []

# states to learn.csv
learn_states =[]


while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States correct ", prompt="whats the another state "
                                                                                            "name ").title()
    if answer_state == "Exit":
        for remain_state in all_state:
            if remain_state not in guess_states:
                learn_states.append(remain_state)
        new_data = pandas.DataFrame(learn_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))
=======
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# funtion used to get the coordinates
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor())

# answer_state = screen.textinput(title="guess the state ", prompt="whats the another state name ")

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
guess_states = []

# states to learn.csv
# learn_states =[]


while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States correct ", prompt="whats the another state "
                                                                                            "name ").title()
    if answer_state == "Exit":
        missing_state = [remain_state for remain_state in all_state if remain_state not in guess_states]
        # for remain_state in all_state:
        #     if remain_state not in guess_states:
        #         learn_states.append(remain_state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))
>>>>>>> master
screen.exitonclick()