import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# print(answer_state)

# check if the guess is among the 50 states

data = pandas.read_csv("50_states.csv")
possible_states = data["state"].to_list()
# print(possible_states)

score = 0
answer_list = []
while len(answer_list) < 50:
    answer_state = screen.textinput(title=f"{len(answer_list)}/50 States correct", prompt="What's another state's name?")
    # convert the guess to title case
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break
    if answer_state in possible_states:
        answer_list.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        row = data[data.state == answer_state]
        tim.goto(int(row.x), int(row.y))
        tim.write(row.state.item())
        score +=1

#we have 2 lists: possible states and answer_list. if an item from possible is not in answer list, output it as a csv

missing = [item for item in possible_states if item not in answer_list]

missingdf = pandas.DataFrame(missing)

missingdf.to_csv("missing_states_csv")


# write correct guesses onto the map
# use a loop to allow the user to keep guessing
# record correct guesses in a list
# keep track of score

#you can tap into the attributes of a row of data using the column headers

# screen.mainloop()
