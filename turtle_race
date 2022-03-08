from turtle import Turtle, Screen
import random

lets_race = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the rase? Enter a color: ")
colors = ["red", "orange", "pink", "green", "blue", "purple"]
y_position = [-125, -75, -25, 25, 75, 125]
my_turtles = []

for turtles in range(6):
    spot = Turtle(shape="turtle")
    spot.penup()
    spot.color(colors[turtles])
    spot.goto(x=-230, y=y_position[turtles])
    my_turtles.append(spot)

if bet:
    lets_race = True

while lets_race:

    for turtle in my_turtles:
        if turtle.xcor() > 230:
            lets_race = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You win! The {winner} turtle is the winner!!!")
            else:
                print(f"You lost! The {winner} turtle is the winner!!!")
        moving = random.randint(0, 10)
        turtle.forward(moving)

screen.exitonclick()
