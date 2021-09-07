import turtle
import pandas as pd

screen = turtle.Screen()
screen2 = turtle.Screen()
screen.title('US State Game')
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()


def missed_states():
    missed = []
    for items in all_states:
        if items in guess:
            pass
        else:
            missed.append(items)
    print(f"Total Correct Answer is : {50 - len(missed)}")
    print(f"Total State missed = {len(missed)}")
    print(missed)
    df = pd.DataFrame(missed)
    df.to_csv('missed_states.csv', index=False, header=False)


guess = []
while len(guess) <= len(all_states):
    answer = screen.textinput(f"{len(guess)}/{len(all_states)}", "Guess the State ").title()
    if answer == 'Exit':
        missed_states()
        break
    elif answer in all_states:
        guess.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
