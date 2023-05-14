import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []
amount = len(guessed_states)

while amount < 50:
    answer_state = screen.textinput(title=f"{amount}/50 States Correct", prompt="What's another state's name?").capitalize()

    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state, font=("Courier", 10, "normal"))
